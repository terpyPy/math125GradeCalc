
from Student import Student

# has access to an instance of Student class variables
class MathClass(Student):
    def __init__(self, sectionNumber, debug=None):
        super().__init__(0, sectionNumber)
        self.sectionNumber = sectionNumber
        self.students:list[Student] = []
        self.names = []
        self.caseDict = {}
    
    def addStudent(self, ID, currentGrade):
        self.students.append(Student(ID, self.sectionNumber, currentGrade))
    
    def getClassAverage(self)->float:
        total = 0
        for student in self.students[1:]:
            total += student.getClassTotal()
        self.classTotal = total/len(self.students)
        return self.classTotal
    
    def getTestAverage(self)->float:
        total = 0
        for student in self.students[1:]:
            total += student.getTestTotal()
        self.testTotal = total/len(self.students)
        return self.testTotal

    def getClassWorkAverage(self)->float:
        total = 0
        for student in self.students[1:]:
            total += student.getClassWorkTotal()
        self.ClassWorkTotal = total/len(self.students)
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
    
    def getStudentNames(self)->list[str]:
        
        self.names = [i.getStudentName() for i in self.students[1:]]
        return self.names
        
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
            if student.getStudentID() < studentName:
                low = mid + 1
            elif student.getStudentID() > studentName:
                high = mid - 1
            else:
                print(i)
                return student.getStudentName(), student.getGrade()
        return 'not found','not found'