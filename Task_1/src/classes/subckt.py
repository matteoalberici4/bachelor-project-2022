# subckt.py

from src.classes.entity import Entity


class Subckt(Entity):
    """
    A sub-circuit object with a given input,
    a given output, and a given operator.
    """
    def __init__(self):
        """
        Construct a 'Subckt' object.

        :return: returns nothing
        """
        super().__init__()
        self._operator = None

    @property
    def operator(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Set the sub-circuit operator.

        :param operator: the sub-circuit operator
        """
        self._operator = operator

    def generate(self, input_=None, operator=None, output=None):
        """
        Generates a sub-circuit object

        :param input_: the sub-circuit input
        :param operator: the sub-circuit operator
        :param output: the sub-circuit output
        :return: returns the sub-circuit object
        """
        self._inputs = input_
        self._operator = operator
        self._outputs = output

        return self
