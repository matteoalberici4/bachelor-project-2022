# circuit_fixers.py

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

            for r in circuit.subckts:
                if r.outputs == s.inputs:

                    for t in circuit.subckts:
                        if t.inputs == s.outputs and t.outputs not in circuit.outputs:

                            r.outputs = t.inputs
                            if s not in gates:
                                gates.append(s)

    # Removing useless gates
    for n in gates:
        circuit.subckts.remove(n)

    return circuit


def remove_not(circuit):
    """
    Removes redundant not gates from a given circuit.

    :param circuit: the circuit to simplify
    :return: returns the simplified circuit
    """
    gates = []

    # Assigning children and parents
    for s in circuit.subckts:
        for t in circuit.subckts:

            if s.outputs == t.inputs:
                s.children.append(t)
                t.parents.append(s)

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
