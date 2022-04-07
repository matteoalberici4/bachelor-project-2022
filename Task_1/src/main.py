#!/usr/bin/env python3

from gv_writer import gv_writer
from PySimpleGUI import Text, In, FolderBrowse, Listbox, Button, Column, VSeperator, Window, WIN_CLOSED
import os


def main():
    """
    Runs the blif-to-gv-translator with a graphical user interface.
    """

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

    # Loop listening for events
    while True:
        event, values = window.read()

        # Stopping the loop
        if event == WIN_CLOSED:
            break

        # Displaying blif files in a folder
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

                window["-FILE_LIST-"].update(files)

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

            except IndexError:
                window["-ERROR-"].update('Please select a different folder.')

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

                # Checking if dot converted the file into pdf
                path = f'{file_name.split(".blif")[0]}.pdf'
                if not os.path.exists(path):
                    raise OSError

                window["-PDF-"].update('PDF: file converted correctly.')

            except OSError:
                window["-PDF-"].update('PDF: dot reported an error while converting.')

            except IndexError:
                window["-ERROR-"].update('Error: please check the syntax of the blif file.')

    # Closing the window
    window.close()


if __name__ == "__main__":
    main()
