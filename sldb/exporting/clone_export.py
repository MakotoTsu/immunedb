from collections import OrderedDict

from sldb.common.models import Clone, CloneStats, Sample
from sldb.exporting.export import Exporter
from sldb.util.nested_writer import NestedCSVWriter


def _if_sample(f, val=''):
    def _wrap(stat):
        if stat.sample_id is not None:
            return f(stat)
        return val
    return _wrap


class CloneExport(Exporter):
    _allowed_fields = OrderedDict({
        'clone_id': lambda s: s.clone_id,
        'sample_id': _if_sample(lambda s: s.sample_id),
        'unique_sequences': lambda s: s.unique_cnt,
        'total_sequences': lambda s: s.total_cnt,

        'v_gene': lambda s: s.clone.v_gene,
        'j_gene': lambda s: s.clone.j_gene,
        'cdr3_nt': lambda s: s.clone.cdr3_nt,
        'cdr3_aa': lambda s: s.clone.cdr3_aa,
        'cdr3_num_nts': lambda s: s.clone.cdr3_num_nts,
        'functional': lambda s: s.clone.cdr3_num_nts % 3 == 0,

        'sample_name': _if_sample(lambda s: s.sample.name, 'Total'),
        'subject_id': _if_sample(lambda s: s.sample.subject.id),
        'subject_identifier':
            _if_sample(lambda s: s.sample.subject.identifier),
        'tissue': _if_sample(lambda s: s.sample.tissue),
        'subset': _if_sample(lambda s: s.sample.subset),
        'disease': _if_sample(lambda s: s.sample.disease),
        'ig_class': _if_sample(lambda s: s.sample.ig_class),
        'v_primer': _if_sample(lambda s: s.sample.v_primer),
        'j_primer': _if_sample(lambda s: s.sample.j_primer),
        'lab': _if_sample(lambda s: s.sample.lab),
        'experimenter': _if_sample(lambda s: s.sample.experimenter),
        'date': _if_sample(lambda s: s.sample.date),
        'tree': _if_sample(lambda s: s.clone.tree),
    })

    def __init__(self, session, rtype, rids, selected_fields):
        super(CloneExport, self).__init__(
            session, rtype, rids, CloneExport._allowed_fields,
            selected_fields)

    def get_data(self):
        csv = NestedCSVWriter(self.selected_fields, streaming=True)
        if self.rtype == 'samples':
            clone_ids = map(
                lambda e: e.clone_id,
                self.session.query(CloneStats.clone_id).filter(
                    CloneStats.sample_id.in_(self.rids)
                ).all()
            )
        else:
            clone_ids = self.rids

        clone_ids = set(clone_ids)
        for clone_id in clone_ids:
            clone = self.session.query(Clone).filter(
                Clone.id == clone_id
            ).one()
            stats = self.session.query(CloneStats).filter(
                CloneStats.clone_id == clone_id
            ).order_by(CloneStats.sample_id)
            for stat in stats:
                yield csv.add_row(self.get_selected_data(stat))
