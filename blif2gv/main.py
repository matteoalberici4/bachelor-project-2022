#!/usr/bin/env python3

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

from src.gv_writer import gv_writer
from PySimpleGUI import Text, In, FolderBrowse, Listbox, Button, Column, VSeperator, Window, WIN_CLOSED
import os
import sys


def main():
    """
    Runs the blif-to-gv translator with a graphical user interface.
    """

    # Text-based User interface
    if len(sys.argv) > 1:

        # Converting the blif file to gv
        try:
            gv_writer(sys.argv[1])
            print(f'File "{sys.argv[1]}" was successfully converted to GV.')

        # Handling IndexError
        except IndexError:
            print('Error: please check the syntax of the blif file.')

        # Checking if the user wants to create a pdf with DOT
        if len(sys.argv) > 2:
            if sys.argv[2] == 'dot':

                # Converting the gv file to pdf
                try:
                    os.system(f'dot -T pdf {sys.argv[1].split(".blif")[0]}.gv -o {sys.argv[1].split(".blif")[0]}.pdf')

                    # Checking if the file was created successfully
                    if os.path.exists(f'{sys.argv[1].split(".blif")[0]}.gv'):
                        print(f'File "{sys.argv[1].split(".blif")[0]}.gv" was successfully converted to pdf.')
                    else:
                        raise OSError

                # Handling OSError
                except OSError:
                    print('There was an error during the process.')

            else:
                print(f'Unknown command "{sys.argv[2]}", consider using "dot".')

    # Graphical User Interface
    else:

        # Displaying the blif files contained in a folder
        files_list = [
            [
                Text('Blif Folder:', font=7),
                In(enable_events=True, key="-BLIF_FOLDER-", size=(25, 1)),
                FolderBrowse()
            ],
            [
                Listbox(enable_events=True, font=7, key="-FILE_LIST-", size=(40, 20), values=[])
            ]
        ]

        # Defining the slot for the file to convert
        blif_file = [
            [
                Text("Choose a blif file from the list.", font=7)
            ],
            [
                Text(font=6, key="-BLIF_FILE-")
            ],
            [
                Button('Convert', enable_events=True, key="-CONVERT-", visible=False)
            ],
        ]

        # Defining the slot for the error handler
        error_handler = [
            [
                Text('', font=6, key="-ERROR-", visible=True)
            ],
            [
                Text('', font=6, key="-GV-", visible=True)
            ],
            [
                Text('', font=6, key="-PDF-", visible=True)
            ]
        ]

        # Defining the window layout
        layout = [
            Column(files_list),
            VSeperator(),
            Column(blif_file + error_handler)
        ]

        # Displaying the window
        window = Window("Blif -> Gv -> Pdf", [layout])

        # Listening for events
        while True:

            event, values = window.read()

            # Stopping the loop
            if event == WIN_CLOSED:
                break

            # Displaying the blif files found in a folder
            elif event == "-BLIF_FOLDER-":

                folder = values["-BLIF_FOLDER-"]

                try:
                    file_list = os.listdir(folder)

                    # Checking whether there is at least one blif file
                    if len(file_list) == 0:
                        raise OSError

                    # Adding files to the list
                    files = [f for f in file_list
                             if os.path.isfile(os.path.join(folder, f))
                             and f.lower().endswith(".blif")]

                    # Sorting the files in alphabetical order
                    files.sort()

                    window["-FILE_LIST-"].update(files)

                # Handling OSError
                except OSError:
                    window["-ERROR-"].update('Please select a different folder.')

            # Selecting a file in the list
            elif event == "-FILE_LIST-":

                try:
                    # Updating the window with the selected file
                    file_name = os.path.join(values["-BLIF_FOLDER-"], values["-FILE_LIST-"][0])
                    window["-BLIF_FILE-"].update(file_name.split('/')[-1])
                    window["-CONVERT-"].update(visible=True)

                    window["-ERROR-"].update('')
                    window["-GV-"].update('')
                    window["-PDF-"].update('')

                # Handling IndexError
                except IndexError:
                    window["-ERROR-"].update('Please select a different folder.')

                # Handling OSError
                except OSError:
                    window["-ERROR-"].update('There was an error during the process.')

            # Converting the selected blif file
            elif event == "-CONVERT-":

                try:
                    file_name = os.path.join(values["-BLIF_FOLDER-"], values["-FILE_LIST-"][0])

                    # Writing the gv file
                    gv_writer(file_name)
                    window["-GV-"].update('GV: file converted correctly.')

                    # Writing the pdf file
                    os.system(f'dot -T pdf {file_name.split(".blif")[0]}.gv -o {file_name.split(".blif")[0]}.pdf')

                    # Checking if DOT converted the file into pdf
                    path = f'{file_name.split(".blif")[0]}.pdf'
                    if not os.path.exists(path):
                        raise OSError

                    window["-PDF-"].update('PDF: file converted correctly.')

                # Handling OSError
                except OSError:
                    window["-PDF-"].update('PDF: dot reported an error while converting.')

                # Handling IndexError
                except IndexError:
                    window["-ERROR-"].update('Error: please check the syntax of the blif file.')

        # Closing the window
        window.close()

    return


# Driver
if __name__ == "__main__":
    main()
