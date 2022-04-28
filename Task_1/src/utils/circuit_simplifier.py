# circuit_simplifier.py

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

def remove_gates(circuit, gates):
    """
    Deletes a set of gates in a circuit.
    
    :param circuit: the circuit to be updated
    :param gates: the gates to be removed
    :return: returns the updated circuit
    """

    # Removing gates
    for n in gates:
        for s in circuit.subckts:

            # Removing children
            if n in s.children:
                s.children.remove(n)

            # Removing parents
            if n in s.parents:
                s.parents.remove(n)

        # Deleting the gate
        circuit.subckts.remove(n)

    return circuit


def remove_assign(circuit):
    """
    Removes useless assign gates from a given circuit.
    Assign gates are useless if they do not lead to a circuit output.

    :param circuit: the circuit to simplify
    :return: returns the simplified circuit
    """

    gates = []

    # Finding useless assign gates
    for s in circuit.subckts:
        if s.operator == 'assign':

            # Resetting parents and children relationships
            for c in s.children:
                if c.outputs not in circuit.outputs:
                    c.inputs = s.inputs
                    c.parents.append(s.parents[0])
                    s.parents[0].children.append(c)

                    # Adding the gate to the useless ones
                    if s not in gates:
                        gates.append(s)

    # Removing useless gates
    circuit = remove_gates(circuit, gates)

    return circuit


def remove_not(circuit):
    """
    Removes redundant not gates from a given circuit.
    Two not gates are redundant if the value taken in input by the second gate's children is equal to the value taken
    in input by the first gate.

    :param circuit: the circuit to simplify
    :return: returns the simplified circuit
    """

    gates = []

    # Finding redundant not gates
    for s in circuit.subckts:
        if s.operator == 'not' and len(s.children) == 1:
            if s.children[0].operator == 'not':

                # Resetting parents and children relationships
                for cc in s.children[0].children:
                    cc.inputs = s.inputs
                    s.parents[0].children.append(cc)
                    cc.parents.append(s.parents[0])

                    # Adding the gates to the useless ones
                    if s not in gates:
                        gates.append(s)
                    if s.children[0] not in gates:
                        gates.append(s.children[0])

    # Removing redundant gates
    circuit = remove_gates(circuit, gates)

    return circuit
