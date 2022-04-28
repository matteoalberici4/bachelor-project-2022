# assign_relatives.py

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

from src.classes.subckt import Subckt


def assign_relatives(circuit):
    """
    Assigns children and parents to every sub-circuit in a circuit.

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
