# Author      : Cameron W. Kerley
# Date        : 5/23/2022
# Description : this is script is used to create a grade book for a math classes
#               each instance of of a math class will have a list of students 
#               and return relevant information. this info is displayed in a table created by this script.
import PySimpleGUI as sg
import studentDataBase as sdb
from sections import Sections


class_list = sdb.main(125)
class_container = Sections(class_list, [class_list.sectionNum])
sectionsDict = class_container.getSectionDict()
buttonPadding = ' '*6
class_Av_button = buttonPadding[:4] + "class average:" + buttonPadding[:4]
test_Av_button = buttonPadding[:4] + "class test avg:" + buttonPadding[:4]
clear_button = buttonPadding[:2] + "change section:" + buttonPadding[:0]
class_work_avg=buttonPadding[:2] + "class work avg:" + buttonPadding[:1]
# program info stuff
progNam = "Grade Book"
verNum = "v1.1.3"
aboutMsg = f'About {progNam} {verNum}'
placeHolder = '_DEFAULT_'
# top menu bar layout
# ------  Menu Definition ------ #    
#  |  -------------------------  |
#  |  | New | graphs | Help      |
#  --------------------------------
# new has more then one possible menu context, 
# the main menu is a logical grouping of the sub-menus events,
# so the sub-menu events should be the events listened for.
menu_def = [['New', ['Student', 'Class Section', 'Exit'  ]],      
                ['graphs', ['scatter plot', placeHolder, placeHolder, ]],      
                ['Help', 'About...'], ]
# this list is used to create the table layout for the student names    
class_list_column = [
   
    
    [sg.Submit(key="-class avg-",
               button_text=class_Av_button),
    sg.Text(str(sectionsDict[1].getClassAverage())[0:5], key="avg")],
    [sg.Submit(key="-test avg-",
               button_text=test_Av_button), 
    sg.Text(str(sectionsDict[1].getTestAverage())[0:5], key="avg test")],
    
    [
        sg.Text("---student grades----"),
        
    ],
    
    [
        sg.Listbox(values=sectionsDict[1].getStudentNames(), 
                   enable_events=True, 
                   size=(60, 30), 
                   key="-grade list-")
    ],
]

# this list is used to create the table layout for the student grades
grade_viewer_column = [
   
    [sg.Submit(key="-show-",
               button_text=clear_button)],
    [sg.Submit(key="-work avg-",
               button_text=class_work_avg),
    sg.Text(str(sectionsDict[1].getClassWorkAverage())[0:5], key="class work avg")],
    
    [sg.Text("Choose a student from list on left:", key="-student name-", size=(24, 1))],
    [sg.Listbox(size=(60, 30),values=["Choose a student"], enable_events=True, key="-chose student-")],
    
]

# version info on screen bottom
bottom_row = [sg.Text(size=(60,1)), sg.Text(size=(45,1)),sg.Text(verNum,)]
# layout for the main window in one data structure
layout = [
    [sg.Menu(menu_def, )],
    [
        sg.Column(class_list_column),
        sg.VSeperator(),
        sg.Column(grade_viewer_column),
    ],
    bottom_row,
    
]

# create the main window with the layout
window = sg.Window(progNam, layout)
sectionNum = 1
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-show-":
        # clear the left listbox and set informational text
        #
        text = sg.popup_get_text("Enter the section number:")
        if text:
            sectionNum = int(text)
            window["-grade list-"].update(sectionsDict[sectionNum].getStudentNames())
            window["-student name-"].update("Choose a student from list on left:")
            window["-chose student-"].update(["Choose a student"])
        
    elif event == 'About...':
        sg.popup(aboutMsg, 
                 'This is a simple grade book program written by: ', 
                 'Cameron Kerley(terpyPY).', 
                 'Github: https://github.com/terpyPy')
        
    elif event == 'Class Section':
        sectionNum = len(sectionsDict) + 1
        class_container.addSection(sectionNum)
        window["-grade list-"].update(sectionsDict[sectionNum].getStudentNames())
        window["-chose student-"].update(["Choose a student"])    
           
    elif event == "Student":
        # create a new student id num from the class list size
        newID = len(sectionsDict[sectionNum].students)
        # create a new student from student _0_ which is the base student to be copied
        # and is not displayed in the listbox
        sectionsDict[sectionNum].addStudent(newID, sectionsDict[sectionNum].getStudent(0)[1].copy())
        sectionsDict[sectionNum].sortStudents()
        window["-grade list-"].update(sectionsDict[sectionNum].getStudentNames())
        
    elif event == "-grade list-":
        # A student was chosen from the listbox, get the student's name
        studentName =  values["-grade list-"][0]
        # get the students id number from the name
        idNum = studentName.split("_")[1]
        sectionNum = int(studentName.split("_")[3])
        # find the student in the class list and get their grade
        gradeList = sectionsDict[sectionNum].getStudent(int(idNum), True)[1]
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
            sectionNum = int(studentName.split("_")[3])
            gradeChosen = values["-chose student-"][0].strip()
            # parse the gradeChosen into a case using first word of gradeChosen output
            case = gradeChosen.split(" ")[0]
            # using the math class change the grade by passing the case and text and idNum
            sectionsDict[sectionNum].studentCase(idNum, text, case)
            # update the right listbox with the student's grades
            gradeList = sectionsDict[sectionNum].getStudent(int(idNum), True)[1]
            window["-chose student-"].update(gradeList) 
          
    elif event == "-class avg-":
        avg = sectionsDict[sectionNum].getClassAverage()
        window["avg"].update(str(avg))
        
    elif event == "-test avg-":
        avg = sectionsDict[sectionNum].getTestAverage()
        window["avg test"].update(str(avg))
    
    elif event == "-work avg-":
        avg = sectionsDict[sectionNum].getClassWorkAverage()
        window["class work avg"].update(str(avg))
    # scatter plot 
    elif event == "scatter plot":
        class_container.showPlot1()
window.close()