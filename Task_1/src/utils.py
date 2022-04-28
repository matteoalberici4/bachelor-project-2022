from classes.subckt import Subckt

# utils.py

# Copyright 2022 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def fix_syntax(string):
    """
    Renames inputs and outputs in order to
    avoid errors in gv syntax.

    :param string: the string to modify
    :return: returns the modified string
    """

    # Splitting long names
    if len(string) > 10:
        string = string[-10:]

    # Removing special characters
    for i in range(len(string)):
        if not string[i].isalnum():
            if i == 0:
                string = string.replace(string[i], 'n')
            else:
                string = string.replace(string[i], '_')

    return string


def assign_relatives(circuit):
    """
    Assigns children and parents to every sub-circuit.

    :param circuit: the circuit to update
    :return: returns the updated circuit
    """

    # Assigning children and parents
    for s in circuit.subckts:

        # Checking for parents in the circuit inputs
        for i in circuit.inputs:
            if s.inputs == i:
                input_node = Subckt().generate('', 'input', i)
                s.parents.append(input_node)

        # Checking for relatives in subcircuits
        for t in circuit.subckts:
            if s.outputs == t.inputs:
                s.children.append(t)
                t.parents.append(s)

    return circuit
