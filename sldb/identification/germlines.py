j = {
    'IGHJ1|4|5':
        'CTGGGGCCAGGGCACCCTGGTCACCGTCTCCTCAG',
    'IGHJ2': 
        'CTACTGGTACTTCGATCTCTGGGGCCGTGGCACCCTGGTCACTGTCTCCTCAG',
    'IGHJ3':
        'TGATGCTTTTGATGTCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAG',
    'IGHJ6':
        'ATTACTACTACTACTACGGTATGGACGTCTGGGGGCAAGGGACCACGGTCACCGTCTCCTCAG',
}

# How many nucleotides from J are upstream of CDR3
j_offset = 31

v = {
    'IGHV1-18': (
        'CAGGTTCAGCTGGTGCAGTCTGGAGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTCTCCTGCAAGGCTTCTGGTTACACCTTT------------ACCAGCTATGGTATCAGC'
        'TGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGATGGATCAGCGCTTAC---'
        '---AATGGTAACACAAACTATGCACAGAAGCTCCAG---GGCAGAGTCACCATGACCACA'
        'GACACATCCACGAGCACAGCCTACATGGAGCTGAGGAGCCTGAGATCTGACGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV1-2': (
        'CAGGTGCAGCTGGTGCAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTCTCCTGCAAGGCTTCTGGATACACCTTC------------ACCGGCTACTATATGCAC'
        'TGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGACGGATCAACCCTAAC---'
        '---AGTGGTGGCACAAACTATGCACAGAAGTTTCAG---GGCAGGGTCACCAGTACCAGG'
        'GACACGTCCATCAGCACAGCCTACATGGAGCTGAGCAGGCTGAGATCTGACGACACGGTC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV1-24': (
        'CAGGTCCAGCTGGTACAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTCTCCTGCAAGGTTTCCGGATACACCCTC------------ACTGAATTATCCATGCAC'
        'TGGGTGCGACAGGCTCCTGGAAAAGGGCTTGAGTGGATGGGAGGTTTTGATCCTGAA---'
        '---GATGGTGAAACAATCTACGCACAGAAGTTCCAG---GGCAGAGTCACCATGACCGAG'
        'GACACATCTACAGACACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCC'
        'GTGTATTACTGTGCAACAGA'
    ),
    'IGHV1-3': (
        'CAGGTCCAGCTTGTGCAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTTTCCTGCAAGGCTTCTGGATACACCTTC------------ACTAGCTATGCTATGCAT'
        'TGGGTGCGCCAGGCCCCCGGACAAAGGCTTGAGTGGATGGGATGGATCAACGCTGGC---'
        '---AATGGTAACACAAAATATTCACAGAAGTTCCAG---GGCAGAGTCACCATTACCAGG'
        'GACACATCCGCGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAAGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV1-45': (
        'CAGATGCAGCTGGTGCAGTCTGGGGCT---GAGGTGAAGAAGACTGGGTCCTCAGTGAAG'
        'GTTTCCTGCAAGGCTTCCGGATACACCTTC------------ACCTACCGCTACCTGCAC'
        'TGGGTGCGACAGGCCCCCGGACAAGCGCTTGAGTGGATGGGATGGATCACACCTTTC---'
        '---AATGGTAACACCAACTACGCACAGAAATTCCAG---GACAGAGTCACCATTACTAGG'
        'GACAGGTCTATGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACAGCC'
        'ATGTATTACTGTGCAAGAAA'
    ),
    'IGHV1-46': (
        'CAGGTGCAGCTGGTGCAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTTTCCTGCAAGGCATCTGGATACACCTTC------------ACCAGCTACTATATGCAC'
        'TGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAATAATCAACCCTAGT---'
        '---GGTGGTAGCACAAGCTACGCACAGAAGTTCCAG---GGCAGAGTCACCATGACCAGG'
        'GACACGTCCACGAGCACAGTCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV1-58': (
        'CAAATGCAGCTGGTGCAGTCTGGGCCT---GAGGTGAAGAAGCCTGGGACCTCAGTGAAG'
        'GTCTCCTGCAAGGCTTCTGGATTCACCTTT------------ACTAGCTCTGCTGTGCAG'
        'TGGGTGCGACAGGCTCGTGGACAACGCCTTGAGTGGATAGGATGGATCGTCGTTGGC---'
        '---AGTGGTAACACAAACTACGCACAGAAGTTCCAG---GAAAGAGTCACCATTACCAGG'
        'GACATGTCCACAAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCCGAGGACACGGCC'
        'GTGTATTACTGTGCGGCAGA'
    ),
    'IGHV1-69': (
        'CAGGTGCAGCTGGTGCAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGTCCTCGGTGAAG'
        'GTCTCCTGCAAGGCTTCTGGAGGCACCTTC------------AGCAGCTATGCTATCAGC'
        'TGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAGGGATCATCCCTATC---'
        '---TTTGGTACAGCAAACTACGCACAGAAGTTCCAG---GGCAGAGTCACGATTACCGCG'
        'GACGAATCCACGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV1-8': (
        'CAGGTGCAGCTGGTGCAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTCTCCTGCAAGGCTTCTGGATACACCTTC------------ACCAGTTATGATATCAAC'
        'TGGGTGCGACAGGCCACTGGACAAGGGCTTGAGTGGATGGGATGGATGAACCCTAAC---'
        '---AGTGGTAACACAGGCTATGCACAGAAGTTCCAG---GGCAGAGTCACCATGACCAGG'
        'AACACCTCCATAAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCC'
        'GTGTATTACTGTGCGAGAGG'
    ),
    'IGHV1-f': (
        'GAGGTCCAGCTGGTACAGTCTGGGGCT---GAGGTGAAGAAGCCTGGGGCTACAGTGAAA'
        'ATCTCCTGCAAGGTTTCTGGATACACCTTC------------ACCGACTACTACATGCAC'
        'TGGGTGCAACAGGCCCCTGGAAAAGGGCTTGAGTGGATGGGACTTGTTGATCCTGAA---'
        '---GATGGTGAAACAATATACGCAGAGAAGTTCCAG---GGCAGAGTCACCATAACCGCG'
        'GACACGTCTACAGACACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCC'
        'GTGTATTACTGTGCAACA'
    ),
    'IGHV2-26': (
        'CAGGTCACCTTGAAGGAGTCTGGTCCT---GTGCTGGTGAAACCCACAGAGACCCTCACG'
        'CTGACCTGCACCGTCTCTGGGTTCTCACTCAGC------AATGCTAGAATGGGTGTGAGC'
        'TGGATCCGTCAGCCCCCAGGGAAGGCCCTGGAGTGGCTTGCACACATTTTTTCGAAT---'
        '------GACGAAAAATCCTACAGCACATCTCTGAAG---AGCAGGCTCACCATCTCCAAG'
        'GACACCTCCAAAAGCCAGGTGGTCCTTACCATGACCAACATGGACCCTGTGGACACAGCC'
        'ACATATTACTGTGCACGGATAC'
    ),
    'IGHV2-5': (
        'CAGATCACCTTGAAGGAGTCTGGTCCT---ACGCTGGTGAAACCCACACAGACCCTCACG'
        'CTGACCTGCACCTTCTCTGGGTTCTCACTCAGC------ACTAGTGGAGTGGGTGTGGGC'
        'TGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCTTGCACTCATTTATTGGAAT---'
        '------GATGATAAGCGCTACAGCCCATCTCTGAAG---AGCAGGCTCACCATCACCAAG'
        'GACACCTCCAAAAACCAGGTGGTCCTTACAATGACCAACATGGACCCTGTGGACACAGCC'
        'ACATATTACTGTGCACACAGACC'
    ),
    'IGHV2-70': (
        'CAGGTCACCTTGAGGGAGTCTGGTCCT---GCGCTGGTGAAACCCACACAGACCCTCACA'
        'CTGACCTGCACCTTCTCTGGGTTCTCACTCAGC------ACTAGTGGAATGTGTGTGAGC'
        'TGGATCCGTCAGCCCCCAGGGAAGGCCCTGGAGTGGCTTGCACTCATTGATTGGGAT---'
        '------GATGATAAATACTACAGCACATCTCTGAAG---ACCAGGCTCACCATCTCCAAG'
        'GACACCTCCAAAAACCAGGTGGTCCTTACAATGACCAACATGGACCCTGTGGACACAGCC'
        'ACGTATTACTGTGCACGGATAC'
    ),
    'IGHV3-11': (
        'CAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCAAGCCTGGAGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTGACTACTACATGAGC'
        'TGGATCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTTTCATACATTAGTAGTAGT---'
        '---GGTAGTACCATATACTACGCAGACTCTGTGAAG---GGCCGATTCACCATCTCCAGG'
        'GACAACGCCAAGAACTCACTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-13': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTACAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTACGACATGCAC'
        'TGGGTCCGCCAAGCTACAGGAAAAGGTCTGGAGTGGGTCTCAGCTATTGGTACTGCT---'
        '------GGTGACACATACTATCCAGGCTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GAAAATGCCAAGAACTCCTTGTATCTTCAAATGAACAGCCTGAGAGCCGGGGACACGGCT'
        'GTGTATTACTGTGCAAGAGA'
    ),
    'IGHV3-15': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTAAAGCCTGGGGGGTCCCTTAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACTTTC------------AGTAACGCCTGGATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTTGGCCGTATTAAAAGCAAAACT'
        'GATGGTGGGACAACAGACTACGCTGCACCCGTGAAA---GGCAGATTCACCATCTCAAGA'
        'GATGATTCAAAAAACACGCTGTATCTGCAAATGAACAGCCTGAAAACCGAGGACACAGCC'
        'GTGTATTACTGTACCACAGA'
    ),
    'IGHV3-20': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGTGTGGTACGGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTT------------GATGATTATGGCATGAGC'
        'TGGGTCCGCCAAGCTCCAGGGAAGGGGCTGGAGTGGGTCTCTGGTATTAATTGGAAT---'
        '---GGTGGTAGCACAGGTTATGCAGACTCTGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACGCCAAGAACTCCCTGTATCTGCAAATGAACAGTCTGAGAGCCGAGGACACGGCC'
        'TTGTATCACTGTGCGAGAGA'
    ),
    'IGHV3-21': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCCTGGTCAAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTATAGCATGAAC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCATCCATTAGTAGTAGT---'
        '---AGTAGTTACATATACTACGCAGACTCAGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACGCCAAGAACTCACTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-23': (
        'GAGGTGCAGCTGTTGGAGTCTGGGGGA---GGCTTGGTACAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTT------------AGCAGCTATGCCATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGCTATTAGTGGTAGT---'
        '---GGTGGTAGCACATACTACGCAGACTCCGTGAAG---GGCCGGTTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCC'
        'GTATATTACTGTGCGAAAGA'
    ),
    'IGHV3-30': (
        'CAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCGTGGTCCAGCCTGGGAGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTATGCTATGCAC'
        'TGGGTCCGCCAGGCTCCAGGCAAGGGGCTAGAGTGGGTGGCAGTTATATCATATGAT---'
        '---GGAAGTAATAAATACTACGCAGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCTGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-30-3': (
        'CAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCGTGGTCCAGCCTGGGAGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTATGCTATGCAC'
        'TGGGTCCGCCAGGCTCCAGGCAAGGGGCTGGAGTGGGTGGCAGTTATATCATATGAT---'
        '---GGAAGCAATAAATACTACGCAGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCTGAGGACACGGCT'
        'GTGTATTACTGTGCGAGA'
    ),
    'IGHV3-33': (
        'CAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCGTGGTCCAGCCTGGGAGGTCCCTGAGA'
        'CTCTCCTGTGCAGCGTCTGGATTCACCTTC------------AGTAGCTATGGCATGCAC'
        'TGGGTCCGCCAGGCTCCAGGCAAGGGGCTGGAGTGGGTGGCAGTTATATGGTATGAT---'
        '---GGAAGTAATAAATACTATGCAGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-43': (
        'GAAGTGCAGCTGGTGGAGTCTGGGGGA---GTCGTGGTACAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTT------------GATGATTATACCATGCAC'
        'TGGGTCCGTCAAGCTCCGGGGAAGGGTCTGGAGTGGGTCTCTCTTATTAGTTGGGAT---'
        '---GGTGGTAGCACATACTATGCAGACTCTGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACAGCAAAAACTCCCTGTATCTGCAAATGAACAGTCTGAGAACTGAGGACACCGCC'
        'TTGTATTACTGTGCAAAAGATA'
    ),
    'IGHV3-48': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTACAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTATAGCATGAAC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTTTCATACATTAGTAGTAGT---'
        '---AGTAGTACCATATACTACGCAGACTCTGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATGCCAAGAACTCACTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-49': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTACAGCCAGGGCGGTCCCTGAGA'
        'CTCTCCTGTACAGCTTCTGGATTCACCTTT------------GGTGATTATGCTATGAGC'
        'TGGTTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTAGGTTTCATTAGAAGCAAAGCT'
        'TATGGTGGGACAACAGAATACACCGCGTCTGTGAAA---GGCAGATTCACCATCTCAAGA'
        'GATGGTTCCAAAAGCATCGCCTATCTGCAAATGAACAGCCTGAAAACCGAGGACACAGCC'
        'GTGTATTACTGTACTAGAGA'
    ),
    'IGHV3-53': (
        'GAGGTGCAGCTGGTGGAGTCTGGAGGA---GGCTTGATCCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGGTTCACCGTC------------AGTAGCAACTACATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGTTATTTATAGCGGT---'
        '------GGTAGCACATACTACGCAGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTTCAAATGAACAGCCTGAGAGCCGAGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-64': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTATGCTATGCAC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGACTGGAATATGTTTCAGCTATTAGTAGTAAT---'
        '---GGGGGTAGCACATATTATGCAAACTCTGTGAAG---GGCAGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTTCAAATGGGCAGCCTGAGAGCTGAGGACATGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-66': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCGTC------------AGTAGCAACTACATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTCTCAGTTATTTATAGCGGT---'
        '------GGTAGCACATACTACGCAGACTCCGTGAAG---GGCAGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTTCAAATGAACAGCCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-7': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTT------------AGTAGCTATTGGATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTGGCCAACATAAAGCAAGAT---'
        '---GGAAGTGAGAAATACTATGTGGACTCTGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACGCCAAGAACTCACTGTATCTGCAAATGAACAGCCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV3-72': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCCAGCCTGGAGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTGACCACTACATGGAC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGGCTGGAGTGGGTTGGCCGTACTAGAAACAAAGCT'
        'AACAGTTACACCACAGAATACGCCGCGTCTGTGAAA---GGCAGATTCACCATCTCAAGA'
        'GATGATTCAAAGAACTCACTGTATCTGCAAATGAACAGCCTGAAAACCGAGGACACGGCC'
        'GTGTATTACTGTGCTAGAGA'
    ),
    'IGHV3-73': (
        'GAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTCCAGCCTGGGGGGTCCCTGAAA'
        'CTCTCCTGTGCAGCCTCTGGGTTCACCTTC------------AGTGGCTCTGCTATGCAC'
        'TGGGTCCGCCAGGCTTCCGGGAAAGGGCTGGAGTGGGTTGGCCGTATTAGAAGCAAAGCT'
        'AACAGTTACGCGACAGCATATGCTGCGTCGGTGAAA---GGCAGGTTCACCATCTCCAGA'
        'GATGATTCAAAGAACACGGCGTATCTGCAAATGAACAGCCTGAAAACCGAGGACACGGCC'
        'GTGTATTACTGTACTAGACA'
    ),
    'IGHV3-74': (
        'GAGGTGCAGCTGGTGGAGTCCGGGGGA---GGCTTAGTTCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTC------------AGTAGCTACTGGATGCAC'
        'TGGGTCCGCCAAGCTCCAGGGAAGGGGCTGGTGTGGGTCTCACGTATTAATAGTGAT---'
        '---GGGAGTAGCACAAGCTACGCGGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACGCCAAGAACACGCTGTATCTGCAAATGAACAGTCTGAGAGCCGAGGACACGGCT'
        'GTGTATTACTGTGCAAGAGA'
    ),
    'IGHV3-9': (
        'GAAGTGCAGCTGGTGGAGTCTGGGGGA---GGCTTGGTACAGCCTGGCAGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCTTT------------GATGATTATGCCATGCAC'
        'TGGGTCCGGCAAGCTCCAGGGAAGGGCCTGGAGTGGGTCTCAGGTATTAGTTGGAAT---'
        '---AGTGGTAGCATAGGCTATGCGGACTCTGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAACGCCAAGAACTCCCTGTATCTGCAAATGAACAGTCTGAGAGCTGAGGACACGGCC'
        'TTGTATTACTGTGCAAAAGATA'
    ),
    'IGHV3-NL1': (
        'CAGGTGCAGCTGGTGGAGTCTGGGGGA---GGCGTGGTCCAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCGTCTGGATTCACCTTC------------AGTAGCTATGGCATGCAC'
        'TGGGTCCGCCAGGCTCCAGGCAAGGGGCTGGAGTGGGTCTCAGTTATTTATAGCGGT---'
        '---GGTAGTAGCACATACTATGCAGACTCCGTGAAG---GGCCGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGTATCTGCAAATGAACAGCCTGAGAGCTGAGGACACGGCT'
        'GTGTATTACTGTGCGAAAGA'
    ),
    'IGHV3-d': (
        'GAGGTGCAGCTGGTGGAGTCTCGGGGA---GTCTTGGTACAGCCTGGGGGGTCCCTGAGA'
        'CTCTCCTGTGCAGCCTCTGGATTCACCGTC------------AGTAGCAATGAGATGAGC'
        'TGGGTCCGCCAGGCTCCAGGGAAGGGTCTGGAGTGGGTCTCATCCATTAGTGGT------'
        '------GGTAGCACATACTACGCAGACTCCAGGAAG---GGCAGATTCACCATCTCCAGA'
        'GACAATTCCAAGAACACGCTGCATCTTCAAATGAACAGCCTGAGAGCTGAGGACACGGCT'
        'GTGTATTACTGTAAGAAA'
    ),
    'IGHV4-28': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCGGACACCCTGTCC'
        'CTCACCTGCGCTGTCTCTGGTTACTCCATCAGC---------AGTAGTAACTGGTGGGGC'
        'TGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTACATCTATTATAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATGTCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGTGGACACGGCC'
        'GTGTATTACTGTGCGAGAAA'
    ),
    'IGHV4-30-2': (
        'CAGCTGCAGCTGCAGGAGTCCGGCTCA---GGACTGGTGAAGCCTTCACAGACCCTGTCC'
        'CTCACCTGCGCTGTCTCTGGTGGCTCCATCAGC------AGTGGTGGTTACTCCTGGAGC'
        'TGGATCCGGCAGCCACCAGGGAAGGGCCTGGAGTGGATTGGGTACATCTATCATAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACAGGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCC'
        'GTGTATTACTGTGCCAGAGA'
    ),
    'IGHV4-30-4': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCACAGACCCTGTCC'
        'CTCACCTGCACTGTCTCTGGTGGCTCCATCAGC------AGTGGTGATTACTACTGGAGT'
        'TGGATCCGCCAGCCCCCAGGGAAGGGCCTGGAGTGGATTGGGTACATCTATTACAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCGAGTTACCATATCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACTGCCGCAGACACGGCC'
        'GTGTATTACTGTGCCAGAGA'
    ),
    'IGHV4-31': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCACAGACCCTGTCC'
        'CTCACCTGCACTGTCTCTGGTGGCTCCATCAGC------AGTGGTGGTTACTACTGGAGC'
        'TGGATCCGCCAGCACCCAGGGAAGGGCCTGGAGTGGATTGGGTACATCTATTACAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCTAGTTACCATATCAGTA'
        'GACACGTCTAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACTGCCGCGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV4-34': (
        'CAGGTGCAGCTACAGCAGTGGGGCGCA---GGACTGTTGAAGCCTTCGGAGACCCTGTCC'
        'CTCACCTGCGCTGTCTATGGTGGGTCCTTC------------AGTGGTTACTACTGGAGC'
        'TGGATCCGCCAGCCCCCAGGGAAGGGGCTGGAGTGGATTGGGGAAATCAATCATAGT---'
        '------GGAAGCACCAACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCT'
        'GTGTATTACTGTGCGAGAGG'
    ),
    'IGHV4-39': (
        'CAGCTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCGGAGACCCTGTCC'
        'CTCACCTGCACTGTCTCTGGTGGCTCCATCAGC------AGTAGTAGTTACTACTGGGGC'
        'TGGATCCGCCAGCCCCCAGGGAAGGGGCTGGAGTGGATTGGGAGTATCTATTATAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATATCCGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCAGACACGGCT'
        'GTGTATTACTGTGCGAGACA'
    ),
    'IGHV4-4': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTCCGGGGACCCTGTCC'
        'CTCACCTGCGCTGTCTCTGGTGGCTCCATCAGC---------AGTAGTAACTGGTGGAGT'
        'TGGGTCCGCCAGCCCCCAGGGAAGGGGCTGGAGTGGATTGGGGAAATCTATCATAGT---'
        '------GGGAGCACCAACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACAAGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCC'
        'GTGTATTGCTGTGCGAGAGA'
    ),
    'IGHV4-59': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCGGAGACCCTGTCC'
        'CTCACCTGCACTGTCTCTGGTGGCTCCATC------------AGTAGTTACTACTGGAGC'
        'TGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTATATCTATTACAGT---'
        '------GGGAGCACCAACTACAACCCCTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCTGCGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV4-61': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCGGAGACCCTGTCC'
        'CTCACCTGCACTGTCTCTGGTGGCTCCGTCAGC------AGTGGTAGTTACTACTGGAGC'
        'TGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTATATCTATTACAGT---'
        '------GGGAGCACCAACTACAACCCCTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCTGCGGACACGGCC'
        'GTGTATTACTGTGCGAGAGA'
    ),
    'IGHV4-b': (
        'CAGGTGCAGCTGCAGGAGTCGGGCCCA---GGACTGGTGAAGCCTTCGGAGACCCTGTCC'
        'CTCACCTGCGCTGTCTCTGGTTACTCCATCAGC---------AGTGGTTACTACTGGGGC'
        'TGGATCCGGCAGCCCCCAGGGAAGGGGCTGGAGTGGATTGGGAGTATCTATCATAGT---'
        '------GGGAGCACCTACTACAACCCGTCCCTCAAG---AGTCGAGTCACCATATCAGTA'
        'GACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCAGACACGGCC'
        'GTGTATTACTGTGCGAGA'
    ),
    'IGHV5-51': (
        'GAGGTGCAGCTGGTGCAGTCTGGAGCA---GAGGTGAAAAAGCCCGGGGAGTCTCTGAAG'
        'ATCTCCTGTAAGGGTTCTGGATACAGCTTT------------ACCAGCTACTGGATCGGC'
        'TGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGATCATCTATCCTGGT---'
        '---GACTCTGATACCAGATACAGCCCGTCCTTCCAA---GGCCAGGTCACCATCTCAGCC'
        'GACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCC'
        'ATGTATTACTGTGCGAGACA'
    ),
    'IGHV5-a': (
        'GAAGTGCAGCTGGTGCAGTCTGGAGCA---GAGGTGAAAAAGCCCGGGGAGTCTCTGAGG'
        'ATCTCCTGTAAGGGTTCTGGATACAGCTTT------------ACCAGCTACTGGATCAGC'
        'TGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGAGGATTGATCCTAGT---'
        '---GACTCTTATACCAACTACAGCCCGTCCTTCCAA---GGCCACGTCACCATCTCAGCT'
        'GACAAGTCCATCAGCACTGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCC'
        'ATGTATTACTGTGCGAGA'
    ),
    'IGHV6-1': (
        'CAGGTACAGCTGCAGCAGTCAGGTCCA---GGACTGGTGAAGCCCTCGCAGACCCTCTCA'
        'CTCACCTGTGCCATCTCCGGGGACAGTGTCTCT------AGCAACAGTGCTGCTTGGAAC'
        'TGGATCAGGCAGTCCCCATCGAGAGGCCTTGAGTGGCTGGGAAGGACATACTACAGGTCC'
        '---AAGTGGTATAATGATTATGCAGTATCTGTGAAA---AGTCGAATAACCATCAACCCA'
        'GACACATCCAAGAACCAGTTCTCCCTGCAGCTGAACTCTGTGACTCCCGAGGACACGGCT'
        'GTGTATTACTGTGCAAGAGA'
    ),
    'IGHV7-4-1': (
        'CAGGTGCAGCTGGTGCAATCTGGGTCT---GAGTTGAAGAAGCCTGGGGCCTCAGTGAAG'
        'GTTTCCTGCAAGGCTTCTGGATACACCTTC------------ACTAGCTATGCTATGAAT'
        'TGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGATGGATCAACACCAAC---'
        '---ACTGGGAACCCAACGTATGCCCAGGGCTTCACA---GGACGGTTTGTCTTCTCCTTG'
        'GACACCTCTGTCAGCACGGCATATCTGCAGATCTGCAGCCTAAAGGCTGAGGACACTGCC'
        'GTGTATTACTGTGCGAGA'
    ),
}
