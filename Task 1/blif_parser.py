#!/usr/bin/env python3

from Ckt import Ckt
from Subckt import Subckt


def generate_ckt(file_name):
    """
    Generates a circuits object by reading a .blif file.

    :param file_name: the name of the .blif file
    :return: returns the circuit object
    """

    # Opening the .blif file
    blif_file = open(file_name, 'r')
    lines = blif_file.readlines()

    circuit_inputs = []
    circuit_outputs = []

    for line in lines:
        # Set the circuit inputs
        if line[0:7] == '.inputs':
            circuit_inputs = line[8:].split(' ')
        # Set the circuit outputs
        if line[0:8] == '.outputs':
            circuit_inputs = line[9:].split(' ')

    # Create the circuit object
    circuit = Ckt()
    circuit.inputs = circuit_inputs
    circuit.outputs = circuit_outputs
    return circuit


def blif_parser(file_name):
    """
    Parses a .blif file in order to obtain a .gv file.

    :param file_name: the name of the .blif file
    :return: returns nothing
    """
    # Generate the circuit object
    circuit = generate_ckt(file_name)

    subckts = []

    # Opening the .blif file
    blif_file = open(file_name, 'r')
    lines = blif_file.readlines()

    for line in lines:

        if line[0:7] == '.subckt':
            expression = line.split(' ')
            # Find the operator
            operator = expression[1]
            # Find the inputs
            inputs = expression[2:-1]
            for i in range(0, len(inputs)):
                inputs[i] = inputs[i].split('=')[1]
            # Find the output
            output = expression[-1].split('=')[1].strip()
            # Create the sub-circuit object
            subckt = Subckt()
            subckt.inputs = inputs
            subckt.operator = operator
            subckt.output = output
            subckts.append(subckt)

    for line in lines:
        # Rename the outputs
        if line[0:6] == '.names' and len(line.split(' ')) == 3:
            new_line = line.split(' ')
            old_name = new_line[1]
            new_name = new_line[2].strip()
            for i in range(0, len(subckts)):
                if subckts[i].output == old_name:
                    subckts[i].output = new_name
    # Update the circuit sub-circuits
    circuit.subckts = subckts

    for s in circuit.subckts:
        print(s.inputs, s.operator, s.output)


blif_parser('abs_diff_8_0.1_re.blif')
