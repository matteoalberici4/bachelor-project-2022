class Ckt:
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
        self._inputs = None
        self._outputs = None
        self._subckts = None

    @property
    def inputs(self):
        """
        Get the circuit inputs.

        :return: returns the circuit inputs
        """
        return self._inputs

    @property
    def outputs(self):
        """
        Get the circuit outputs.

        :return: returns the circuit outputs
        """
        return self._outputs

    @property
    def subckts(self):
        """
        Get the circuit sub-circuits.

        :return: returns the circuit sub-circuits
        """
        return self._subckts

    @inputs.setter
    def inputs(self, inputs):
        """
        Set the circuit inputs.

        :param inputs: the circuit inputs
        """
        self._inputs = inputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Set the circuit outputs.

        :param outputs: the circuit outputs
        """
        self._outputs = outputs

    @subckts.setter
    def subckts(self, subckts):
        """
        Set the circuit sub-circuits.

        :param subckts: the circuit sub-circuits
        """
        self._subckts = subckts
