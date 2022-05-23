import time
from mathClass import MathClass
import random
import gradeCalc


def main(numStudents=1000, ui: bool = False) -> MathClass:
    startTime = time.time()
    schoolClass = MathClass(1)
    # msgs:str = 'Initializing...'
    for i in range(numStudents):
        # sg.one_line_progress_meter('Making students',
        #                            i+1,
        #                            numStudents,
        #                            'key',
        #                            msgs,
        #                            makeStudent(schoolClass, i))
        makeStudent(schoolClass, i)

    runTime = time.time() - startTime
    print(f'Time to create class: {runTime}')
    schoolClass.sortStudents()
    return schoolClass


def makeStudent(schoolClass: MathClass, i) -> str:
    test = [[4, 3],
            [
        [random.randrange(25, 100),
         random.randrange(45, 100),
         random.randrange(65, 100)],
        random.randrange(30, 100)],
        random.randrange(40, 100),
        random.randrange(60, 100)
    ]
    studentGrades = gradeCalc.uiVersion(test)
    schoolClass.addStudent(i, studentGrades)

    # return schoolClass.students[i].getStudentName() + 'loaded...'


if __name__ == '__main__':
    x = main(20000)
