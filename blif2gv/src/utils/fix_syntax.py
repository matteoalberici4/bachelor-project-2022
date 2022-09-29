# fix_syntax.py

# Copyright 2022 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

def fix_syntax(name):
    """
    Renames inputs and outputs in order to avoid errors in the GV syntax.

    :param name: the string to modify
    :return: returns the modified string
    """

    # Splitting long names
    if len(name) > 10:
        name = name[-10:]

    # Ensuring there is a letter at the beginning
    if not name[0].isalpha():
        name = name.replace(name[0], 'n')

    # Removing special characters
    for i in range(1, len(name)):
        if not name[i].isalnum():
            name = name.replace(name[i], '_')

    return name
