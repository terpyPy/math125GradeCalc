class Student:
    def __init__(self, ID, sectionNum, currentGrade:str='default, default, default, default'):
        self.studentID = ID
        self.sectionNum = sectionNum
        self.name = 'student_' + str(ID)+'_section_'+str(self.sectionNum)+'_'
        if isinstance(currentGrade, str):
            self.currentGrade = currentGrade.split(",")[:4]
        else:
            self.currentGrade = currentGrade
        self.classTotal = self.currentGrade[0]
        self.testTotal = self.currentGrade[1]
        self.classWorkTotal = self.currentGrade[2]
        self.checkAndSetsTotal = self.currentGrade[3]
       
    def setclassTotal(self, grade:str):
        Total = self.classTotal.split(" ")
        Total[3] = str(float(grade)) + '%'
        self.classTotal = ' '.join(Total)
        self.currentGrade[0] = self.classTotal
        
    def setTestTotal(self, grade:str):
        Total = self.testTotal.split(" ")
        Total[4] = str(float(grade))
        self.testTotal = ' '.join(Total)
        self.currentGrade[1] = self.testTotal
    
    def setClassWorkTotal(self, grade:str):
        Total = self.classWorkTotal.split(" ")
        Total[4] = str(float(grade))
        self.classWorkTotal = ' '.join(Total)
        self.currentGrade[2] = self.classWorkTotal
    
    def setCheckAndSetsTotal(self, grade:str):
        Total = self.checkAndSetsTotal.split(" ")
        Total[5] = str(float(grade))
        self.checkAndSetsTotal = ' '.join(Total)
        self.currentGrade[3] = self.checkAndSetsTotal
    
    def getGrade(self)->str:
        return self.currentGrade
    
    def getClassTotal(self):
        Total = self.classTotal.split(" ")
        num = float(Total[3][:-1])
        return num
    
    def getClassWorkTotal(self):
        Total = self.classWorkTotal.split(" ")
        num = float(Total[4][:-1]) / 0.25
        return num
    
    def getTestTotal(self):
        Total = self.testTotal.split(" ")
        num = float(Total[4][:-1]) / (0.15 *4)
        return num
    
    def getStudentID(self):
        return int(self.studentID)
    
    def getStudentName(self):
        return self.name