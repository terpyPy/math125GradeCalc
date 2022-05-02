import PySimpleGUI as sg
import studentDataBase as sdb
import gradeEntryHandler as geh


file_list_column = [
   
    [
        sg.Text("student grades"),
        sg.Submit(key="-show-",button_text="show"),
    ],
    
    [
        sg.Listbox(values=[], 
                   enable_events=True, 
                   size=(40, 20), 
                   key="-grade list-")
    ],
]

grade_viewer_column = [
   
    [sg.Text("Choose a student from list on left:", key="-student name-")],
    [sg.Listbox(size=(40, 20),values=[], enable_events=True, key="-student-")],
]

layout = [
    
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(grade_viewer_column),
    ]
]

window = sg.Window("Grade Book", layout)

file_list = sdb.main(100)
names = [i.getStudentName() for i in file_list.students]

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-show-":
        # Get list of grades
        
        window["-grade list-"].update(names)
        window["-student name-"].update("Choose a student from list on left:")
        window["-student-"].update([])
    elif event == "-grade list-":  # A student was chosen from the listbox
            filename =  values["-grade list-"][0]
            idNum = filename.split("_")[1]
            gradeList = file_list.getStudent(int(idNum), True)[1]
            window["-student name-"].update(filename)
            window["-student-"].update(gradeList)
            
    elif event == "-student-":
        # lazy way to handle user closing popup, and change not saving
        try:
            filename =  values["-grade list-"][0]
            idNum = filename.split("_")[1]
            gradeChosen = values["-student-"][0].strip()
            
            text = sg.popup_get_text('enter new grade for entry:')
            geh.entryHandler(gradeChosen, file_list, idNum, gradeList, window, text)
            
        except:
            print("not_found")
window.close()