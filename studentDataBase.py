from Student import Student
from mathClass import MathClass
import random
import gradeCalc
import PySimpleGUI as sg


def main(numStudents=1000, ui:bool=False)->MathClass:
    schoolClass = MathClass(1, [])
    msgs:str = 'Initializing...'
    for i in range(numStudents):
        sg.one_line_progress_meter('Making students', 
                                   i+1, 
                                   numStudents, 
                                   'key', 
                                   msgs,
                                   makeStudent(schoolClass, i))
        
    # runTime = time.time() - startTime
    # print(f'Time to create class: {runTime}')
    schoolClass.students.sort(key=lambda x: x.getStudentID())
    return schoolClass
        
def makeStudent(schoolClass, i)->Student:
    test = [[4,3],
                [
                    [random.randrange(50,100),
                    random.randrange(50,100),
                    random.randrange(50,100)],
                    random.randrange(50,100)],
                random.randrange(70,100),
                random.randrange(60,100)
                ]
    studentGrades = gradeCalc.uiVersion(test)
    schoolClass.addStudent(Student(i, schoolClass.sectionNumber, studentGrades))
    
    return schoolClass.students[i].getStudentName() + 'loaded...'
    
if __name__ == '__main__':
    x = main(1000)