import PySimpleGUI as sg
import studentDataBase as sdb
# import gradeEntryHandler as geh
class_list = sdb.main(100)

buttonPadding = ' '*6
class_Av_button = buttonPadding[:4] + "class average:" + buttonPadding[:4]
test_Av_button = buttonPadding[:4] + "class test avg:" + buttonPadding[:4]
clear_button = buttonPadding + "clear list:" + buttonPadding
class_work_avg=buttonPadding[:2] + "class work avg:" + buttonPadding[:1]
# program info stuff
progNam = "Grade Book"
verNum = "v1.1.0"
aboutMsg = f'About {progNam} {verNum}'
# top menu bar layout
# ------  Menu Definition ------ #    
#  |  -------------------------  |
#  |  | New  Edit  Help       |  |
#  --------------------------------
# new has more then one possible menu context, 
# the main menu is a logical grouping of the sub-menus events,
# so the sub-menu events should be the events listened for.
menu_def = [['New', ['Student', 'Class Section', 'Exit'  ]],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]
      
class_list_column = [
   
    
    [sg.Submit(key="-class avg-",
               button_text=class_Av_button),
    sg.Text(str(class_list.getClassAverage())[0:5], key="avg")],
    [sg.Submit(key="-test avg-",
               button_text=test_Av_button), 
    sg.Text(str(class_list.getTestAverage())[0:5], key="avg test")],
    
    [
        sg.Text("---student grades----"),
        
    ],
    
    [
        sg.Listbox(values=class_list.getStudentNames(), 
                   enable_events=True, 
                   size=(60, 30), 
                   key="-grade list-")
    ],
]

grade_viewer_column = [
   
    [sg.Submit(key="-show-",
               button_text=clear_button)],
    [sg.Submit(key="-work avg-",
               button_text=class_work_avg),
    sg.Text(str(class_list.getClassWorkAverage())[0:5], key="class work avg")],
    
    [sg.Text("Choose a student from list on left:", key="-student name-", size=(24, 1))],
    [sg.Listbox(size=(60, 30),values=["Choose a student"], enable_events=True, key="-chose student-")],
    
]

bottom_row = [sg.Text(size=(60,1)), sg.Text(size=(45,1)),sg.Text(verNum,)]
layout = [
    [sg.Menu(menu_def, )],
    [
        sg.Column(class_list_column),
        sg.VSeperator(),
        sg.Column(grade_viewer_column),
    ],
    bottom_row,
    
]


window = sg.Window(progNam, layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-show-":
        # clear the left listbox and set informational text
        #
        window["-student name-"].update("Choose a student from list on left:")
        window["-chose student-"].update(["Choose a student"])
        
    elif event == 'About...':
        sg.popup(aboutMsg, 
                 'This is a simple grade book program written by: ', 
                 'Cameron Kerley(terpyPY).', 
                 'Github: https://github.com/terpyPy')
        
    elif event == "Student":
        # create a new student id num from the class list size
        newID = len(class_list.students)
        # create a new student from student _0_ which is the base student to be copied
        # and is not displayed in the listbox
        class_list.addStudent(newID, class_list.getStudent(0)[1].copy())
        class_list.sortStudents()
        window["-grade list-"].update(class_list.getStudentNames())
        
    elif event == "-grade list-":
        # A student was chosen from the listbox, get the student's name
        studentName =  values["-grade list-"][0]
        # get the students id number from the name
        idNum = studentName.split("_")[1]
        # find the student in the class list and get their grade
        gradeList = class_list.getStudent(int(idNum), True)[1]
        #
        # update the right listbox with the student's grades,
        # and set the student's name in the text box.
        window["-student name-"].update(studentName)# <-THIS IS REQUIRED FOR RETRIVING STUDENT ID NUMBER AND OVER ALL FUNCTIONALITY.
        window["-chose student-"].update(gradeList)
            
    elif (event == "-chose student-") and ("Choose a student" not in values["-chose student-"]):
        # A grade was chosen from the listbox and not default msg
        text = sg.popup_get_text('enter new grade for entry:')
        # then get the entry to change and the student's id number  
        if text and (text[0].isnumeric() and text[-1].isnumeric()):
            idNum =  values["-grade list-"][0].split("_")[1]
            gradeChosen = values["-chose student-"][0].strip()
            # parse the gradeChosen into a case using first word of gradeChosen output
            case = gradeChosen.split(" ")[0]
            # using the math class change the grade by passing the case and text and idNum
            class_list.studentCase(idNum, text, case)
            # update the right listbox with the student's grades
            gradeList = class_list.getStudent(int(idNum), True)[1]
            window["-chose student-"].update(gradeList) 
          
    elif event == "-class avg-":
        avg = class_list.getClassAverage()
        window["avg"].update(str(avg))
        
    elif event == "-test avg-":
        avg = class_list.getTestAverage()
        window["avg test"].update(str(avg))
    
    elif event == "-work avg-":
        avg = class_list.getClassWorkAverage()
        window["class work avg"].update(str(avg)) 
    
window.close()