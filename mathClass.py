
# Author      : Cameron W. Kerley
# Date        : 5/23/2022
# Description : is extended by sections class container called "sections"
#               has access to an instance of Student class variables. will be used to create a grade book
#               each instance of of a math class will have a list of 
#               students and return the over all averages and retrieve the student names/IDs
from Student import Student
import numpy as np
#
# TODO: No current TODO's 
class MathClass(Student):
    def __init__(self, sectionNumber=-1, grades='default, default, default, default'):
        self.sectionNum = sectionNumber
        super().__init__(0, self.sectionNum, grades)
        self.students:list[Student] = []
        self.names = []
        self.caseDict = {}
    
    def addStudent(self, ID, currentGrade, sectionNumber=None):
        if sectionNumber is None:
            self.students.append(Student(ID, self.sectionNum, currentGrade))
        else:
            self.students.append(Student(ID, sectionNumber, currentGrade))
    
    def getClassAverage(self)->float:
        self.classTotal = sum([i.getClassTotal() for i in self.students[1:]])/(len(self.students)-1)
        return self.classTotal
        # for student in self.students[1:]:
        #     total += student.getClassTotal()
        # self.classTotal = total/len(self.students)
        # return self.classTotal
    
    def getTestAverage(self)->float:
        self.testTotal = sum([i.getTestTotal() for i in self.students[1:]])/(len(self.students)-1)
        # for student in self.students[1:]:
        #     total += student.getTestTotal()
        # self.testTotal = total/len(self.students)
        return self.testTotal

    def getClassWorkAverage(self)->float:
        self.ClassWorkTotal = sum([i.getClassWorkTotal() for i in self.students[1:]])/(len(self.students)-1)
        # for student in self.students[1:]:
        #     total += student.getClassWorkTotal()
        # self.ClassWorkTotal = total/len(self.students)
        return self.ClassWorkTotal

    def sortStudents(self):
        self.students.sort(key=lambda x: x.getStudentID())
    
    def studentCase(self, idNum, text,case):
        
        self.caseDict = {"current": self.students[int(idNum)].setclassTotal,
                    "test": self.students[int(idNum)].setTestTotal,
                    "class": self.students[int(idNum)].setClassWorkTotal,
                    "checks": self.students[int(idNum)].setCheckAndSetsTotal,
                    None: "not_found"}
        self.caseDict[case](text)
        self.caseDict.clear()
    
    def getStudentNames(self)->'list[str]':
        
        self.names = [i.getStudentName() for i in self.students[1:]]
        return self.names
    def getStudentPlot(self)->'list[float]':
        self.plot1 = np.array([i.getClassTotal() for i in self.students[1:]])
        self.plot2 = np.array([i.getTestTotal() for i in self.students[1:]]) 
        return self.plot1, self.plot2
        
    def getStudent(self, studentName:int,UI=False):
        # binary search for student
        low = 0
        high = len(self.students) - 1
        mid = 0
        i = 0
        while low <= high:
            i+=1
            mid = (low + high) // 2
            student:Student = self.students[mid]
            if int(student.getStudentID()) < studentName:
                low = mid + 1
            elif int(student.getStudentID()) > studentName:
                high = mid - 1
            else:
                print(i)
                return student.getStudentName(), student.getGrade()
        return 'not found','not found'