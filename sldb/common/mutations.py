import json

from sqlalchemy import distinct

from sldb.common.models import Sequence, SequenceCollapse
import sldb.util.lookups as lookups
import sldb.util.funcs as funcs


class ContextualMutations(object):
    def __init__(self, regions):
        self._seen = {}
        self._regions = regions
        self._pos_seen = set([])
        self.region_muts = {}
        self.position_muts = {}

    def add_mutation(self, seq, cdr3_num_nts, mutation, from_aa,
                     intermediate_seq_aa, final_seq_aa, copy_number):
        pos, _, _, mtype = mutation
        region = funcs.get_pos_region(self._regions, cdr3_num_nts, pos)
        self._add_to_region(seq, cdr3_num_nts, mutation, from_aa,
                            intermediate_seq_aa, final_seq_aa, copy_number,
                            region)
        self._add_to_region(seq, cdr3_num_nts, mutation, from_aa,
                            intermediate_seq_aa, final_seq_aa, copy_number,
                            'ALL')

        if pos not in self.position_muts:
            self.position_muts[pos] = {}
        if mtype not in self.position_muts[pos]:
            self.position_muts[pos][mtype] = 0
        self.position_muts[pos][mtype] += 1

    def _add_to_region(self, seq, cdr3_num_nts, mutation, from_aa,
                       intermediate_seq_aa, final_seq_aa, copy_number, region):
        pos, from_nt, to_nt, mtype = mutation
        if region not in self.region_muts:
            self.region_muts[region] = {}

        # If it's a new mutation, setup the dictionaries
        if mtype not in self.region_muts[region]:
            self.region_muts[region][mtype] = {}

        if mutation not in self.region_muts[region][mtype]:
            self.region_muts[region][mtype][mutation] = {
                'pos': pos,
                'from_nt': from_nt,
                'from_aa': from_aa,
                'to_nt': to_nt,
                'to_aas': [],

                'unique': 0,
                'total': 0,
                'intermediate_aa': intermediate_seq_aa,
            }

        mut_dict = self.region_muts[region][mtype][mutation]
        if final_seq_aa not in mut_dict['to_aas']:
            mut_dict['to_aas'].append(final_seq_aa)

        mut_dict['unique'] += 1
        mut_dict['total'] += copy_number

    def get_all(self):
        # Strip the dictionary keys and just make a list of mutations
        final_regions = {}
        for region, types in self.region_muts.iteritems():
            final_regions[region] = {}
            for mtype, mutations in types.iteritems():
                final_regions[region][mtype] = mutations.values()

        return {
            'regions': final_regions,
            'positions': self.position_muts
        }


class CloneMutations(object):
    MODE_SAMPLES_AND_TOTAL = 0
    MODE_SAMPLES_ONLY = 1
    MODE_TOTAL_ONLY = 2

    def __init__(self, session, clone):
        self._clone = clone
        self._session = session
        self._germline = self._clone.consensus_germline

    def _get_codon_at(self, seq, i):
        aa_off = i - i % 3
        return seq[aa_off:aa_off + 3]

    def _get_aa_at(self, seq, i):
        return lookups.aa_from_codon(self._get_codon_at(seq, i))

    def _get_mutation(self, seq, i):
        if (self._germline[i] != seq[i] and
                self._germline[i] != 'N' and
                seq[i] != 'N'):
            grm_aa = self._get_aa_at(self._germline, i)
            # Simulate this mutation alone
            off = i % 3
            grm_codon = self._get_codon_at(self._germline, i)
            seq_aa = lookups.aa_from_codon(
                grm_codon[:off] + seq[i] + grm_codon[off+1:])

            if grm_aa is None or seq_aa is None:
                return 'unknown', seq_aa
            elif grm_aa != seq_aa:
                if lookups.are_conserved_aas(grm_aa, seq_aa):
                    return 'conservative', seq_aa
                return 'nonconservative', seq_aa
            else:
                return 'synonymous', seq_aa

        return None, None

    def calculate(self, commit_seqs=False, limit_samples=None):
        sample_mutations = {}

        if limit_samples is not None:
            sample_ids = limit_samples
        else:
            sample_ids = map(lambda r: r.sample_id, self._session.query(
                distinct(Sequence.sample_id).label('sample_id')
                ).filter(
                Sequence.clone == self._clone
                ).all()
            )
            sample_ids.append(None)

        for sample_id in sample_ids:
            seqs = self._session.query(Sequence).filter(
                Sequence.clone == self._clone)
            if sample_id is None:
                seqs = seqs.join(SequenceCollapse).filter(
                    SequenceCollapse.copy_number_in_subject > 0
                )
            else:
                seqs = seqs.filter(
                    Sequence.sample_id == sample_id
                )
            sample_mutations[sample_id] = self._get_contextual_mutations(
                seqs, commit_seqs, use_sample_copy=sample_id is not None)

        return sample_mutations

    def _get_contextual_mutations(self, seqs, commit_seqs, use_sample_copy):
        context_mutations = ContextualMutations(self._clone.regions)
        for seq in seqs:
            seq_mutations = {}
            for i in range(0, len(seq.clone_sequence)):
                mtype, intermediate_aa = self._get_mutation(
                    seq.clone_sequence, i)
                if mtype is None:
                    continue

                from_aa = self._get_aa_at(self._germline, i)
                seq_mutations[i] = mtype

                mutation = (i, self._germline[i], seq.clone_sequence[i], mtype)
                copy_field = (
                    seq.copy_number if use_sample_copy else
                    seq.collapse.copy_number_in_subject
                )
                context_mutations.add_mutation(
                    seq.clone_sequence, self._clone.cdr3_num_nts,
                    mutation, from_aa, intermediate_aa,
                    self._get_aa_at(seq.clone_sequence, i), copy_field)

            if commit_seqs:
                seq.mutations_from_clone = json.dumps(seq_mutations)
        return context_mutations


def threshold_mutations(all_muts, min_required_seqs):
    final = {}
    for region, types in all_muts['regions'].iteritems():
        final[region] = {
            'counts': {
                'total': {},
                'unique': {}
            },
            'mutations': {}
        }
        for mtype, mutations in types.iteritems():
            for mutation in mutations:
                if mutation['unique'] >= min_required_seqs:
                    if mtype not in final[region]['mutations']:
                        final[region]['mutations'][mtype] = []
                    if mtype not in final[region]['counts']['total']:
                        final[region]['counts']['total'][mtype] = 0
                        final[region]['counts']['unique'][mtype] = 0
                    final[region]['mutations'][mtype].append(mutation)
                    final[region]['counts']['total'][mtype] += \
                        mutation['unique']
                    final[region]['counts']['unique'][mtype] += 1
    return final
