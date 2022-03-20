#!/usr/bin/env python3

from ckt import Ckt
from subckt import Subckt


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
            circuit_outputs = line[9:].split(' ')
    circuit_inputs[-1] = circuit_inputs[-1][:-1]
    circuit_outputs[-1] = circuit_outputs[-1][:-1]

    # Close the blif file
    blif_file.close()

    # Create the circuit object
    circuit = Ckt()
    circuit.inputs = circuit_inputs
    circuit.outputs = circuit_outputs
    return circuit


def blif_parser(file_name):
    """
    Parses a .blif file in order to obtain a .gv file.

    :param file_name: the name of the .blif file
    :return: returns the created circuit
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
            operator = expression[1][1:]

            # Find the inputs
            inputs = expression[2:-1]
            for i in range(0, len(inputs)):
                inputs[i] = inputs[i].split('=')[1]
            # Find the output
            output = expression[-1].split('=')[1].strip()

            # Create the sub-circuit object
            for i in inputs:
                subckt = Subckt()
                subckt.inputs = i
                subckt.operator = operator
                subckt.output = output
                subckts.append(subckt)

        if line[0:6] == '.names' and len(line.split(' ')) == 3:
            expression = line.split(' ')
            # for o in circuit.outputs:
            #     if o == expression[2].strip():
            subckt = Subckt()
            subckt.operator = 'assign'
            subckt.inputs = expression[1]
            subckt.output = expression[2].strip()
            subckts.append(subckt)

    # Close the .blif file
    blif_file.close()

    # Update the circuit sub-circuits
    circuit.subckts = subckts

    for i in range(0, len(circuit.subckts)):
        if circuit.subckts[i].inputs[0] == '$':
            circuit.subckts[i].inputs = 'n' + circuit.subckts[i].inputs.split(':')[1].replace("$", '').replace('_', '')
        if circuit.subckts[i].output[0] == '$':
            circuit.subckts[i].output = 'n' + circuit.subckts[i].output.split(':')[1].replace("$", '').replace('_', '')

    return circuit
