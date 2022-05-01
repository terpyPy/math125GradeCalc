class Student:
    def __init__(self, ID, sectionNum, currentGrade:str='default'):
        self.studentID = ID
        self.sectionNum = sectionNum
        self.name = 'student_' + str(ID)+'_section_'+str(self.sectionNum)+'_'
        self.currentGrade = currentGrade
    
    def getGrade(self)->str:
        return self.currentGrade
    
    def getStudentID(self):
        return self.studentID
    def getStudentName(self):
        return self.name