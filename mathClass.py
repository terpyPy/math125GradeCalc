
from Student import Student


class MathClass:
    def __init__(self, sectionNumber, students:list, debug=None):
        self.sectionNumber = sectionNumber
        self.students = students
    
    def addStudent(self, student):
        self.students.append(student)
    
    def getStudent(self, studentName:int,UI=False):
        # binary search for student
        low = 0
        high = len(self.students) - 1
        mid = 0
        # i = 0
        while low <= high:
            # i+=1
            mid = (low + high) // 2
            student:Student = self.students[mid]
            if student.getStudentID() < studentName:
                low = mid + 1
            elif student.getStudentID() > studentName:
                high = mid - 1
            else:
                # print(i)
                return student.getStudentName(), student.getGrade()
        return 'not found','not found'