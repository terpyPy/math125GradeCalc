from Student import Student
from mathClass import MathClass
import random
import gradeCalc
# import time

def main(debug=100)->None:
    # startTime = time.time()
    schoolClass = MathClass(1, [])
   
    for i in range(debug):
        test = [[4,3],
                [
                    [random.randrange(50,100),
                    random.randrange(50,100),random.randrange(50,100)],
                    random.randrange(50,100)],
                random.randrange(70,100),
                random.randrange(60,100)
                ]
        studentGrades = gradeCalc.main(debug=test)
        schoolClass.addStudent(Student(i, schoolClass.sectionNumber, studentGrades))
    # runTime = time.time() - startTime
    # print(f'Time to create class: {runTime}')
    schoolClass.students.sort(key=lambda x: x.getStudentID())
    return schoolClass
        

if __name__ == '__main__':
    x = main(1000)