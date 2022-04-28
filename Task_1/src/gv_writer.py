# gv_writer.py

# Copyright 2022 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

from blif_parser import blif_parser


def gv_writer(file_name):
    """
    Writes a gv file from a blif file.

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
    outputs = []
    for s in circuit.subckts:
        if s.outputs not in outputs:
            gv_file.write(f'    {s.outputs} [label="')
            gv_file.write(f'{s.operator}\\n\\n{s.outputs}", fillcolor=white]\n')
            outputs.append(s.outputs)

    # Writing circuit outputs
    for i in range(len(circuit.outputs)):
        gv_file.write(f'    {circuit.outputs[i]} [label="out{str(i)}')
        gv_file.write(f'\\n{circuit.outputs[i]}", shape=doublecircle, fillcolor=white]\n')

    # Writing edges: input -> output
    gv_file.write('    edge [fontname=Geneva, fontcolor=forestgreen]\n')
    for s in circuit.subckts:
        gv_file.write(f'    {s.inputs} -> {s.outputs}\n')

    # Closing the gv file
    gv_file.write('}')
    gv_file.close()

    # Printing if every operation was performed successfully.
    print(f'File "{file_name}" converted successfully.')

    return
