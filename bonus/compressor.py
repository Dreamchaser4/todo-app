import PySimpleGUI as cp

label1 = cp.Text("Select files to compress :")
input1 = cp.Input()
choose_button1 = cp.FileBrowse("Choose")

label2 = cp.Text("Select files to compress :")
input2 = cp.Input()
choose_button2 = cp.FileBrowse("Choose")

compress_button = cp.Button("Compress")

window = cp.Window('File Compressor', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],
                                              [compress_button]])
window.read()
window.close()