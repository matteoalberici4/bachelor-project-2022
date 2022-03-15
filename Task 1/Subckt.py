class Subckt:
    """
    A sub-circuit object with a given set of inputs,
    a given output, and a given operator.
    """
    def __init__(self):
        """
        Construct a 'Subckt' object.

        :return: returns nothing
        """
        self._inputs = None
        self._operator = None
        self._output = None

    @property
    def inputs(self):
        """
        Get the sub-circuit inputs.

        :return: returns the sub-circuit inputs
        """
        return self._inputs

    @property
    def operator(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self._operator

    @property
    def output(self):
        """
        Get the sub-circuit output.

        :return: returns the sub-circuit output
        """
        return self._output

    @inputs.setter
    def inputs(self, inputs):
        """
        Set the sub-circuit inputs.

        :param inputs: the sub-circuit inputs
        """
        self._inputs = inputs

    @operator.setter
    def operator(self, operator):
        """
        Set the sub-circuit operator.

        :param operator: the sub-circuit operator
        """
        self._operator = operator

    @output.setter
    def output(self, output):
        """
        Set the sub-circuit output.

        :param output: the sub-circuit output
        """
        self._output = output
