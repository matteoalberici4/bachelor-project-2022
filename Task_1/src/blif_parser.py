# blif_parser.py

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

from classes.ckt import Ckt
from classes.subckt import Subckt
from truth_tables import unary_gates, binary_gates
from utils.assign_relatives import assign_relatives
from utils.circuit_simplifier import remove_assign, remove_not
from utils.fix_syntax import fix_syntax


def simplify_circuit(circuit):
    """
    Simplifies a given circuit in order to avoid redundant and useless gates.

    :param circuit: the circuit to be simplified
    :return: returns the simplified circuit
    """

    # Fixing circuit inputs syntax
    for i in range(len(circuit.inputs)):
        circuit.inputs[i] = fix_syntax(circuit.inputs[i])

    # Fixing circuit outputs syntax
    for o in range(len(circuit.outputs)):
        circuit.outputs[o] = fix_syntax(circuit.outputs[o])

    # Fixing circuit sub-circuits syntax
    for s in circuit.subckts:
        s.inputs = fix_syntax(s.inputs)
        s.outputs = fix_syntax(s.outputs)

    # Removing useless assign gates
    circuit = remove_assign(circuit)

    # Removing redundant not gates
    circuit = remove_not(circuit)

    return circuit


def blif_parser(file_name):
    """
    Parses a blif file translating it into a gv file.

    :param file_name: the name of the blif file
    :return: returns the updated circuit
    """

    # Generating the circuit object
    circuit = Ckt().generate(file_name)

    # Defining the sub-circuits list
    subckts = []

    # Opening the blif file
    blif_file = open(file_name, 'r')
    lines = blif_file.readlines()

    # Creating the circuit sub-circuits
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

            # Finding the operator truth table
            while lines[i + j][0][0] != '.':
                truth_table.append(lines[i + j].strip())
                j += 1

            # Getting the unary expression
            if len(line) == 3:

                # Searching for the correspondent unary operator
                for operator, table in unary_gates.items():

                    # Creating the sub-circuit object
                    if truth_table == table or truth_table in table:
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

    # Assigning the sub-circuits to the circuit
    circuit.subckts = subckts

    # Assigning sub-circuits parents and children
    circuit = assign_relatives(circuit)

    # Simplifying the circuit
    circuit = simplify_circuit(circuit)

    return circuit
