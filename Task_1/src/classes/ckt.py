# ckt.py

from src.classes.entity import Entity


class Ckt(Entity):
    """
    A circuit object with a given set of inputs,
    a given set of outputs, and a set of sub-circuits
    objects.
    """
    def __init__(self):
        """
        Construct a 'Ckt' object.

        :return: returns nothing
        """
        super().__init__()
        self._subckts = None

    @property
    def subckts(self):
        """
        Get the circuit sub-circuits.

        :return: returns the circuit sub-circuits
        """
        return self._subckts

    @subckts.setter
    def subckts(self, subckts):
        """
        Set the circuit sub-circuits.

        :param subckts: the circuit sub-circuits
        """
        self._subckts = subckts

    def generate(self, file_name=None):
        """
        Generates a circuit object by reading a blif file.

        :param file_name: the name of the blif file
        :return: returns the circuit object
        """

        # Opening the blif file
        blif_file = open(file_name, 'r')
        lines = blif_file.readlines()

        # Defining variables
        circuit_inputs = []
        circuit_outputs = []

        # Loop for setting inputs and outputs
        for line in lines:
            # Set the circuit inputs
            if line[0:7] == '.inputs':
                circuit_inputs = line[8:].split(' ')
            # Set the circuit outputs
            if line[0:8] == '.outputs':
                circuit_outputs = line[9:].split(' ')

        # Removing '\n' from the end of inputs and outputs
        circuit_inputs[-1] = circuit_inputs[-1][:-1]
        circuit_outputs[-1] = circuit_outputs[-1][:-1]

        # Closing the blif file
        blif_file.close()

        # Creating the circuit object
        self._inputs = circuit_inputs
        self._outputs = circuit_outputs

        return self
