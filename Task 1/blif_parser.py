#!/usr/bin/env python3

class Ckt:
    """
    A circuit object with a given set of inputs,
    a given set of outputs, and a set of sub-circuits
    objects.
    """
    def __init__(self, inputs, outputs, subckts):
        """
        Construct a 'Ckt' object.

        :param inputs: the circuit inputs
        :param outputs: the circuit outputs
        :param subckts: the set of sub-circuits creating
        the circuit
        :return: returns nothing
        """
        self.inputs = inputs
        self.outputs = outputs
        self.subckts = subckts

    def get_inputs(self):
        """
        Get the circuit inputs

        :return: returns the circuit inputs
        """
        return self.inputs

    def get_outputs(self):
        """
        Get the circuit outputs

        :return: returns the circuit outputs
        """
        return self.outputs

    def get_subckts(self):
        """
        Get the circuit sub-circuits

        :return: returns the circuit sub-circuits
        """
        return self.subckts


class Subckt:
    """
    A sub-circuit object with a given set of inputs,
    a given output, and a given operator.
    """
    def __init__(self, inputs, operator, output):
        """
        Construct a 'Subckt' object.

        :param inputs: the sub-circuit inputs
        :param operator: the sub-circuit operator
        :param output: the sub-circuit output
        :return: returns nothing
        """
        self.inputs = inputs
        self.operator = operator
        self.output = output

    def get_inputs(self):
        """
        Get the sub-circuit inputs.

        :return: returns the sub-circuit inputs
        """
        return self.inputs

    def get_operator(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self.operator

    def get_output(self):
        """
        Get the sub-circuit output.

        :return: returns the sub-circuit output
        """
        return self.output


def blif_parser():
    """
    Parses a .blif file in order to obtain a .gv file.

    :return: returns nothing
    """
    file1 = open('abs_diff_8_0.1_re.blif', 'r')
    lines = file1.readlines()

    circuit_inputs = []
    circuit_outputs = []
    subckts = []

    for line in lines:
        if line[0:7] == '.inputs':
            circuit_inputs = line[8:].split(' ')
        if line[0:8] == '.outputs':
            circuit_inputs = line[9:].split(' ')
        elif line[0:7] == '.subckt':
            words = line.split(' ')
            operator = words[1]
            inputs = words[2:-1]
            for i in range(0, len(inputs)):
                inputs[i] = inputs[i].split('=')[1]
            output = words[-1].split('=')[1].strip()
            subckt = Subckt(inputs, operator, output)
            subckts.append(subckt)

    for line in lines:
        if line[0:6] == '.names' and len(line.split(' ')) == 3:
            new_line = line.split(' ')
            old_name = new_line[1]
            new_name = new_line[2].strip()
            for i in range(0, len(subckts)):
                if subckts[i].output == old_name:
                    subckts[i].output = new_name

    for i in range(0, len(subckts)):
        print(subckts[i].inputs, subckts[i].operator, subckts[i].output)

    circuit = Ckt(circuit_inputs, circuit_outputs, subckts)

    for s in circuit.subckts:
        print(s.inputs, s.operator, s.output)


blif_parser()
