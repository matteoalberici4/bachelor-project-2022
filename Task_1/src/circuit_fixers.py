# circuit_fixers.py

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


def remove_assign(circuit):
    """
    Removes useless assign gates from a given circuit.
    Assign gates ar useless if they do not lead to a
    circuit output.

    :param circuit: the circuit to simplify
    :return: returns the simplified circuit
    """
    gates = []

    # Finding the useless assign gates
    for s in circuit.subckts:
        if s.operator == 'assign':

            for c in s.children:
                if c.outputs not in circuit.outputs:
                    c.inputs = s.inputs

                    if s not in gates:
                        gates.append(s)

    # Removing useless gates
    for n in gates:
        for s in circuit.subckts:

            if n in s.children:
                s.children.remove(n)

            if n in s.parents:
                s.parents.remove(n)

        circuit.subckts.remove(n)

    return circuit


def remove_not(circuit):
    """
    Removes redundant not gates from a given circuit.

    :param circuit: the circuit to simplify
    :return: returns the simplified circuit
    """
    gates = []

    # Finding redundant not gates
    for s in circuit.subckts:
        if s.operator == 'not' and len(s.children) == 1:

            if s.children[0].operator == 'not' and len(s.children[0].children) == 1:
                s.children[0].children[0].inputs = s.inputs
                gates.append(s.children[0])
                gates.append(s)

    # Removing redundant gates
    for n in gates:
        circuit.subckts.remove(n)

    return circuit
