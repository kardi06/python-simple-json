import PySimpleGUI as sg

label1 = sg.Text("Select File to Compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")
window = sg.Window("File compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])
window.read()
window.close()