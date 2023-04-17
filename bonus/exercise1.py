import PySimpleGUI as ex

label1 = ex.Text("Enter feet:")
input1 = ex.Input()

label2 = ex.Text("Enter inches:")
input2 = ex.Input()

convert_button = ex.Button("Convert")

window = ex.Window('Convertor', layout=[[label1, input1], [label2, input2],
                                              [convert_button]])
window.read()
window.close()
