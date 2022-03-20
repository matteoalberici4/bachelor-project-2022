#!/usr/bin/env python3

from blif_parser import blif_parser
import graphviz


def gv_writer(file_name):
    """
    Writes a .gv file from a .blif file given in
    input.

    :param file_name: the name of the .blif file
    :return: returns nothing
    """
    circuit = blif_parser(file_name)

    # Write the initial information lines
    gv_file = open(file_name.split('.blif')[0] + '.gv', 'w')
    gv_file.write('digraph circuit {\n')
    gv_file.write('    node [style = filled, fillcolor = white,shape=rect, fontname=geneva]\n')

    # Write circuit inputs
    for i in range(0, len(circuit.inputs)):
        gv_file.write('    ' + circuit.inputs[i] + ' [label="in' + str(i))
        gv_file.write('\\nw",shape=circle,fillcolor=white]\n')

    # Write circuit gates
    for i in range(0, len(circuit.subckts)):
        gv_file.write('    ' + circuit.subckts[i].output + ' [label="')
        gv_file.write(circuit.subckts[i].operator + '\\nw",fillcolor=white]\n')

    # Write circuit outputs
    for i in range(0, len(circuit.outputs)):
        gv_file.write('    ' + circuit.outputs[i] + ' [label="out' + str(i))
        gv_file.write('\\nw",shape=doublecircle,fillcolor=white]\n')

    # Write edges
    gv_file.write('    edge [fontname=Geneva,fontcolor=forestgreen]\n')
    for i in range(0, len(circuit.subckts)):
        gv_file.write('    ' + circuit.subckts[i].inputs + '->' + circuit.subckts[i].output + '\n')

    # Close the .gv file
    gv_file.write('}')
    gv_file.close()


# Run the code
gv_writer('../blif/abs_diff_8_0.1_re.blif')
