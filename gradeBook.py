# Author      : Cameron W. Kerley
# Date        : 5/23/2022
# Description : this is script is used to create a grade book for a math classes
#               each instance of of a math class will have a list of students 
#               and return relevant information. this info is displayed in a table created by this script.
import sys
import PySimpleGUI as sg
from sections import Sections
from UI_layout import WindowLayout
# import studentDataBase as sdb
def update_Columns_FIELDS(secNum, secDict):
    print('__update_columns_EVENT__\n')
    # update both listboxes, and display section nums view.
    secDict[secNum].sortStudents()
    window["-grade list-"].update(secDict[secNum].getStudentNames())
    window["-chose student-"].update(["Choose a student"])
    window["-student name-"].update("Choose a student from list on left:")
    class_container.section_numbers.sort()
    window['-sect view-'].update(str(class_container.section_numbers)[1:-1])
    # sectionNum = secNum

def event_matchers(eventFromLoop, secNumFromLoop, vals):
    secNumFromLoop = first_event_matcher(eventFromLoop, secNumFromLoop,vals)
    return secNumFromLoop

def first_event_matcher(eventFromLoop, secNumFromLoop, vals):
    
    match eventFromLoop:
        # calculation cases
        case "-class avg-":
            avg = sectionsDict[secNumFromLoop].getClassAverage()
            window["avg"].update(str(avg)[0:5])
            return secNumFromLoop
    
        case "-test avg-":
            avg = sectionsDict[secNumFromLoop].getTestAverage()
            window["avg test"].update(str(avg)[0:5])
            return secNumFromLoop
    
        case "-work avg-":
            avg = sectionsDict[secNumFromLoop].getClassWorkAverage()
            window["class work avg"].update(str(avg)[0:5])
            return secNumFromLoop
        
        case "-show-":
            # clear the left listbox and set informational text
            #
            text = sg.popup_get_text("Enter the section number:",modal=True)
            if text != None:
                secNumFromLoop = int(text)
                update_Columns_FIELDS(secNumFromLoop, sectionsDict)
            return secNumFromLoop
        
        case _:
            print(f'__event__ <{eventFromLoop}> not a calc__event sec#: {secNumFromLoop}')
            return second_event_matcher(eventFromLoop, secNumFromLoop, vals)

def second_event_matcher(eventFromLoop, secNumFromLoop, vals):
    # toolBar cases
    match eventFromLoop:
        case 'delete student' if len(sectionsDict[secNumFromLoop].students) > 1:
            idToDel = sg.popup_get_text('please enter the students ID number' + 
                                        'NOT FULLY QUALIFIED NAME!')
            sectionsDict[secNumFromLoop].deleteStudent(int(idToDel))
            update_Columns_FIELDS(secNumFromLoop, sectionsDict)
            return secNumFromLoop
        
        case 'Create Section':
            secNumFromLoop =  int(sg.popup_get_text('provide a section number:'+
                                                '(whole numbers only)',
                                                modal=True))
            class_container.addSection(secNumFromLoop)
            update_Columns_FIELDS(secNumFromLoop, sectionsDict)
            return secNumFromLoop
    
        case 'About...':
            sg.popup(aboutMsg, 
                    'This is a simple grade book program written by: ', 
                    'Cameron Kerley(terpyPY).', 
                    'Github: https://github.com/terpyPy')
            return secNumFromLoop
    
        case 'scatter plot':
            class_container.showPlot1()
            return secNumFromLoop
        
        case 'Save':
            f_FORMAT = '.txt'
            f_NAME_WINDOW = sg.popup_get_file('Save Class Grade file as?\n'+
                                    '(forbidden characters "_" and ".")',
                                    modal=True)
            #
            # ---------MUST FORMAT LIKE "<filename>_<section number>.txt"--------"
            # IMPORTANT: this  has be so for all files read in!!!!!.
            qualifiedFileName = f'{f_NAME_WINDOW}_{secNumFromLoop}{f_FORMAT}'
            if f_NAME_WINDOW:
                class_container.saveToFile(qualifiedFileName, section_number=secNumFromLoop)
            return secNumFromLoop
        
        case 'Load':
            grades_file = sg.popup_get_file('Select a .txt file to load', modal=True)
            secNumFromLoop = class_container.addSection(file_name=grades_file)
            update_Columns_FIELDS(secNumFromLoop, sectionsDict)
            return secNumFromLoop
        
        case 'Create Student':
            # create a new student id num from the student with the highest IDnum
            lastStudentNum = sectionsDict[secNumFromLoop].students[-1].getStudentID()
            newID = lastStudentNum + 1
            # create a new student from student _0_ which is the base student to be copied
            # and is not displayed in the listbox
            sectionsDict[secNumFromLoop].addStudent(newID, sectionsDict[secNumFromLoop].getStudent(0)[1].copy())
            update_Columns_FIELDS(secNumFromLoop, sectionsDict,)
            return secNumFromLoop
        
        case _:
            print(f'__event__ <{eventFromLoop}> not a toolBar__event sec#: {secNumFromLoop}')
            return third_event_matcher(eventFromLoop, secNumFromLoop, vals)

def third_event_matcher(eventFromLoop, secNumFromLoop, vals):
    match eventFromLoop:
        case "-grade list-" if vals["-grade list-"] != []:
            # A student was chosen from the listbox, get the student's name    
            studentName =  vals["-grade list-"][0]
            # get the students id number from the name
            idNum, secNumFromLoop, gradeList = get_Window_ID_sectionNum(studentName, vals, secNumFromLoop)
            # find the student in the class list and get their grade
            #
            # set the student's name in the text box.
            window["-student name-"].update(studentName)# <-THIS IS REQUIRED FOR RETRIEVING STUDENT ID NUMBER AND OVER ALL FUNCTIONALITY.
            # update the right listbox with the student's grades,
            window["-chose student-"].update(gradeList)
            return secNumFromLoop
        case "-chose student-" if ("Choose a student" not in vals["-chose student-"]):
            # A grade was chosen from the listbox and not default msg
            text = sg.popup_get_text('enter new grade for entry:', modal=True)
            # then get the entry to change and the student's id number  
            if text and (text[0].isnumeric() and text[-1].isnumeric()):
                studentName =  vals["-grade list-"][0]
                idNum, secNumFromLoop, gradeList = get_Window_ID_sectionNum(studentName, vals, secNumFromLoop)
                gradeChosen = vals["-chose student-"][0].strip()
                # parse the gradeChosen into a case using first word of gradeChosen output
                case = gradeChosen.split(" ")[0]
                # using the math class change the grade by passing the case and text and idNum
                sectionsDict[secNumFromLoop].studentCase(idNum, text, case)
                # update the right listbox with the student's grades
                window["-chose student-"].update(gradeList)
            return secNumFromLoop
            
        case _:
            print(f'__event__ <{eventFromLoop}> not a Display_select_event sec#: {secNumFromLoop}')
            return secNumFromLoop

def get_Window_ID_sectionNum(name, vals, secNumFromLoop):
    print(f'__get_Window_ID_sectionNum_EVENT__ on : {name}\n')
    idNum =  vals["-grade list-"][0].split("_")[1]
    secNum = int(name.split("_")[3])
    gradeList = sectionsDict[secNumFromLoop].getStudent(int(idNum))[1]
    return idNum, secNum, gradeList

init_grades_file = sg.popup_get_file('Select a .txt file to load',modal=True)
if init_grades_file and init_grades_file.endswith('.txt'):
    class_container = Sections(fileName=init_grades_file)
else:
    sys.exit()
    
sectionsDict = class_container.getSectionDict()
# get initial data for display.
initAvgList = (str(sectionsDict[class_container.section_numbers[0]].getClassAverage())[0:5],
               str(sectionsDict[class_container.section_numbers[0]].getTestAverage())[0:5],
               sectionsDict[class_container.section_numbers[0]].getStudentNames(),
               str(class_container.section_numbers)[1:-1],
               str(sectionsDict[class_container.section_numbers[0]].getClassWorkAverage())[0:5])

# layout for the main window in one data structure
layout = WindowLayout(initAvgList)
aboutMsg = layout.get_about_txt()
layout, progNam = layout.get_window_elements()
# create the main window with the layout
window = sg.Window(progNam, layout)
sectionNum = class_container.getInitSecNum()

def main(window, sectionNum):
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # check the chain of events that modify the section number, 
        # one event in the chain when encountered will return the relevant section number.
        # The return value will either be the result of state change, otherwise returns curr section.
        sectionNum = event_matchers(event, sectionNum, values)
                      
    window.close()

if __name__ == "__main__":
    main(window, sectionNum)