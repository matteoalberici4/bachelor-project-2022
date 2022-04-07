# entity.py

from abc import abstractmethod


class Entity:
    """
    An entity object with a given set
    of inputs and a given set of outputs.
    """
    def __init__(self):
        """
        Construct an entity.

        :return: returns nothing
        """
        self._inputs = None
        self._outputs = None

    @property
    def inputs(self):
        """
        Get the entity inputs.

        :return: returns the entity inputs
        """
        return self._inputs

    @property
    def outputs(self):
        """
        Get the entity outputs.

        :return: returns the entity outputs
        """
        return self._outputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Set the entity inputs.

        :param inputs: the entity inputs
        """
        self._inputs = inputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Set the entity outputs.

        :param outputs: the entity outputs
        """
        self._outputs = outputs

    @abstractmethod
    def generate(self):
        pass
