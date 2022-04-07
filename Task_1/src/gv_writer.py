# gv_writer.py

from blif_parser import blif_parser


def gv_writer(file_name):
    """
    Writes a gv file from a blif file given in input.

    :param file_name: the name of the blif file
    :return: returns nothing
    """

    # Parsing the blif file
    circuit = blif_parser(file_name)

    # Writing the initial information lines
    gv_file = open(file_name.split('.blif')[0] + '.gv', 'w')
    gv_file.write('digraph circuit {\n')
    gv_file.write('    node[style=filled, fillcolor=white, shape=rect, fontname=geneva]\n')

    # Writing circuit inputs
    for i in range(len(circuit.inputs)):
        gv_file.write(f'    {circuit.inputs[i]} [label="in{str(i)}')
        gv_file.write(f'\\n{circuit.inputs[i]}", shape=circle, fillcolor=white]\n')

    # Writing circuit gates
    for i in range(len(circuit.subckts)):
        gv_file.write(f'    {circuit.subckts[i].outputs} [label="')
        gv_file.write(f'{circuit.subckts[i].operator}\\n{circuit.subckts[i].outputs}", fillcolor=white]\n')

    # Writing circuit outputs
    for i in range(len(circuit.outputs)):
        gv_file.write(f'    {circuit.outputs[i]} [label="out{str(i)}')
        gv_file.write(f'\\n{circuit.outputs[i]}", shape=doublecircle, fillcolor=white]\n')

    # Writing edges: input -> output
    gv_file.write('    edge [fontname=Geneva, fontcolor=forestgreen]\n')
    for i in range(len(circuit.subckts)):
        gv_file.write(f'    {circuit.subckts[i].inputs} -> {circuit.subckts[i].outputs}\n')

    # Closing the gv file
    gv_file.write('}')
    gv_file.close()

    print(f'File "{file_name}" converted successfully.')

    return
