import PySimpleGUI as ex

label1 = ex.Text("Select files to compress:")
input1 = ex.Input()
choose_button1 = ex.FileBrowse("Choose", key="files")

label2 = ex.Text("Select destination folder:")
input2 = ex.Input()
choose_button2 = ex.FolderBrowse("Choose", key="folder")

compress_button = ex.Button("Compress")

window = ex.Window('File Compressor', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],
                                              [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]

window.close()
