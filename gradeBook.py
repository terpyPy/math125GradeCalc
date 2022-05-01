import os
import PySimpleGUI as sg
import studentDataBase as sdb

file_list_column = [
    [
        sg.Text("student grades"),
        sg.Submit(key="-show-",button_text="show"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-grade list-"
        )
    ],
]

grade_viewer_column = [
    [sg.Text("Choose an student from list on left:")],
    [sg.Text(size=(40, 20),key="-student-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(grade_viewer_column),
    ]
]

window = sg.Window("Grade Book", layout)

file_list = sdb.main()
names = [file_list.students[i].getStudentName() for i in range(len(file_list.students))]
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-show-":
        # Get list of grades
        
        window["-grade list-"].update(names)
        
    elif event == "-grade list-":  # A student was chosen from the listbox
        try:
            filename =  values["-grade list-"][0]
            idNum = filename.split("_")[1]
            t = file_list.getStudent(int(idNum))
            window["-student-"].update('\n'.join(t))
        except:
            pass