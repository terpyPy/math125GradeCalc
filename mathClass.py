
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
        self.IDs = []
        self.caseDict = {}
        self.loggingNotice2 = 'found and removed @ index:'
        
    
    def addStudent(self, ID, currentGrade, sectionNumber=None):
        if sectionNumber is None:
            self.students.append(Student(ID, self.sectionNum, currentGrade))
        else:
            self.students.append(Student(ID, sectionNumber, currentGrade))
    
    def getClassAverage(self)->float:
        if len(self.students) >1:
            self.classTotal = sum([i.getClassTotal() for i in self.students[1:]])/(len(self.students)-1)
            return self.classTotal
       
    
    def getTestAverage(self)->float:
        if len(self.students) >1:
            self.testTotal = sum([i.getTestTotal() for i in self.students[1:]])/(len(self.students)-1)
            return self.testTotal

    def getClassWorkAverage(self)->float:
        if len(self.students) >1:
            self.ClassWorkTotal = sum([i.getClassWorkTotal() for i in self.students[1:]])/(len(self.students)-1)
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
    def getStudentLstGrades(self)->'list[str]':
        return [i.getGrade() for i in self.students[1:]]
    
    def getStudentPlot(self)->'list[float]':
        self.plot2 = np.array([i.getClassTotal() for i in self.students[1:]])
        self.plot1 = np.array([i.getTestTotal() for i in self.students[1:]]) 
        return self.plot1, self.plot2
        
    def getStudent(self, studentName:int, getID=False)->'int|str|None|list[str, str]':
        # binary search for student
        low = 0
        high = len(self.students)-1
        mid = 0
        i = 0
        while (low <= high):
            i+=1
            mid = (low + high) // 2 # 
            student:Student = self.students[mid]
            if int(student.getStudentID()) < studentName:
                low = mid + 1
            elif int(student.getStudentID()) > studentName:
                high = mid - 1
            else:
                name = student.getStudentName()
                print(f'search depth:{i},  student: {name}\n')
                match getID:
                    case True:
                        return mid, name
                    case False:
                        return student.getStudentName(), student.getGrade()
                    case _:
                        print(f'__ERROR__{__file__}encountered None bool for match _recived_: {getID}')
                        return '__ERROR__'
        if getID == True:
            return None, None
        else:               
            return '#', '#'
        
    def deleteStudent(self,IDnum):
        ID_index, name = self.getStudent(IDnum, getID=True)
        if None not in (ID_index, name): 
            del self.students[ID_index]
            self.loggingNoticePrint(ID_index, name)
        
        