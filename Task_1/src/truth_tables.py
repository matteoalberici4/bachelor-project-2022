# truth_tables.py

from itertools import permutations


def permute(gate, combinations):
    """
    Generates all the possible combination for
    representing the truth table of a gate.

    :param gate: the initial representation
    :param combinations: the representations to
        be permuted
    :return: returns all the possible representations
    """
    for elem in permutations(combinations):
        gate.append(list(elem))

    return gate


# Unary operators
unary_gates = {
    'zero': ['- 0'],
    'one': permute(['- 1'], ['0 1', '1 1']),
    'not': ['0 1'],
    'assign': ['1 1']
}

# Binary operators
binary_gates = {
    'zero': ['-- 0'],
    'and': ['11 1'],
    'not_imply': ['10 1'],
    'one_dc': permute(['1- 1'], ['10 1', '11 1']),
    'zero_one': ['01 1'],
    'dc_one': permute(['-1 1'], ['01 1, 11 1']),
    'xor': permute([], ['01 1', '10 1']),
    'or': permute([['1- 1', '-1 1'], ['-1 1', '1- 1']], ['01 1', '10 1', '11 1']),
    'nor': ['00 1'],
    'equality': permute([], ['00 1', '11 1']),
    'dc_zero': permute(['-0 1'], ['00 1', '10 1']),
    'zero_dc': permute(['0- 1'], ['00 1', '01 1']),
    'one': permute(['-- 1'], ['00 1', '01 1', '10 1', '11 1']),
    'not_zero_one': permute([['-0 1', '1- 1'], ['1- 1', '-0 1']], ['00 1', '10 1', '11 1']),
    'imply': permute([['0- 1', '-1 1'], ['-1 1', '0- 1']], ['00 1', '01 1', '11 1']),
    'nand': permute([['0- 1', '-0 1'], ['-0 1', '0- 1']], ['00 1', '01 1', '10 1'])
}
