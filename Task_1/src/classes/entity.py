# entity.py

# Copyright 2022 Matteo Alberici
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
