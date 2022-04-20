# subckt.py

# Copyright 2021 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .entity import Entity


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
        self._children = None
        self._parents = None

    @property
    def operator(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self._operator

    @property
    def children(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self._children

    @property
    def parents(self):
        """
        Get the sub-circuit operator.

        :return: returns the sub-circuit operator
        """
        return self._parents

    @operator.setter
    def operator(self, operator):
        """
        Set the sub-circuit operator.

        :param operator: the sub-circuit operator
        """
        self._operator = operator

    @children.setter
    def children(self, children):
        """
        Set the sub-circuit operator.

        :param children: the sub-circuit children
        """
        self._children = children

    @parents.setter
    def parents(self, parents):
        """
        Set the sub-circuit operator.

        :param parents: the sub-circuit parents
        """
        self._parents = parents

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
        self._children = []
        self._parents = []

        return self
