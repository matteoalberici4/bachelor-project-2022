# blif_parser.py

from src.classes.ckt import Ckt
from src.classes.subckt import Subckt
from truth_tables import unary_gates, binary_gates


def fix_syntax(string):
    """
    Renames inputs and outputs in order to
    avoid errors in gv syntax.

    :param string: the string to modify
    :return: returns the modified string
    """
    for i in range(len(string)):
        if not string[i].isalnum():
            if i == 0:
                string = string.replace(string[i], 'n')
            else:
                string = string.replace(string[i], '_')

    return string


def blif_parser(file_name):
    """
    Parses a blif file in order to obtain a gv file.

    :param file_name: the name of the blif file
    :return: returns the updated circuit
    """

    # Generating the circuit object
    circuit = Ckt().generate(file_name)

    # Defining the subckts list
    subckts = []

    # Opening the blif file
    blif_file = open(file_name, 'r')
    lines = blif_file.readlines()

    # Loop for creating subckts
    i = 0
    while i in range(len(lines)):
        line = lines[i].split(' ')

        # Subckt lines: .subckt operator input(s) output
        if line[0] == '.subckt':

            # Getting the inputs
            inputs = line[2:-1]
            # Getting the operator
            operator = line[1][1:]
            # Getting the output
            output = line[-1].split('=')[1].strip()

            # Creating the sub-circuit object(s)
            for j in inputs:
                input_ = j.split('=')[1]
                subcircuit = Subckt().generate(input_, operator, output)
                subckts.append(subcircuit)

        # Names lines: .names input(s) output
        elif line[0] == '.names' and len(line) > 2:
            truth_table = []
            j = 1
            while lines[i + j][0][0] != '.':
                truth_table.append(lines[i+j].strip())
                j += 1

            # Getting the unary expression
            if len(line) == 3:
                # Searching for the correspondent unary operator
                for operator, table in unary_gates.items():
                    if truth_table == table or truth_table in table:
                        # Creating the sub-circuit object
                        output = line[2].strip()
                        subcircuit = Subckt().generate(line[1], operator, output)
                        subckts.append(subcircuit)
                        break

            # Getting the binary expression
            elif len(line) == 4:
                # Searching for the correspondent binary operator
                for operator, table in binary_gates.items():
                    if truth_table == table or truth_table in table:
                        inputs = [line[1], line[2]]
                        # Creating the sub-circuit object(s)
                        for j in inputs:
                            output = line[3].strip()
                            subcircuit = Subckt().generate(j, operator, output)
                            subckts.append(subcircuit)
                        break

        i += 1

    # Closing the blif file
    blif_file.close()

    # Updating the circuit sub-circuits
    circuit.subckts = subckts

    # Fixing syntax
    for s in circuit.subckts:
        s.inputs = fix_syntax(s.inputs)
        s.outputs = fix_syntax(s.outputs)

    # Removing useless assign gates
    nodes = []
    for s in circuit.subckts:
        if s.operator == 'assign':

            for r in circuit.subckts:
                if r.outputs == s.inputs:

                    for t in circuit.subckts:
                        if t.inputs == s.outputs and t.outputs not in circuit.outputs:

                            r.outputs = t.inputs
                            if s not in nodes:
                                nodes.append(s)

    for n in nodes:
        circuit.subckts.remove(n)

    return circuit
