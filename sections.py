from mathClass import MathClass
import matplotlib.pyplot as plt
import numpy 
# get all the methods needed from sklearn for RMSE 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# TODO: add file IO for this to save to and read from a file
# need to modify the class to be able to read from a file so the constructor 
# needs to be modified to take a file name as a parameter
# ------good way to parse fileName and sectionNum from absPath returned by pop up-----
#           fileNameContents = fileName.split('/')[-1:]
#           file_sec_num = fileNameContents[0].split('_')[1].split('.')[0]
class Sections(MathClass):
    def __init__(self, fileName:str=None, math_class:MathClass=None, section_numbers:'list[int]'=[-1]):
        if math_class is not None:
            self.section_numbers = section_numbers
            self.sectionsDict = {self.section_numbers[0]: math_class}
        elif fileName is not None:
            
            self.section_numbers = section_numbers
            # create an empty classSection with the first section number
            self.sectionsDict = {self.section_numbers[0]: MathClass(self.section_numbers[0])}
            self.sectionsDict[self.section_numbers[0]].addStudent(0,
                                                                'current grade is:--- 0.0%,'+
                                                                'test point total is:--- 0.00 / 60.0,'+
                                                                'class work total is:--- 0.0 / 25.0,'+
                                                                'checks & sets total is:--- 0.0 / 15.0,'
                                                                )
            self.INIT_SEC_NUM = self.readFromFile(fileName)
            
    def getInitSecNum(self):
        return self.INIT_SEC_NUM        
    
    def addSection(self, section_number:int=-1, file_name:str=None)->int|None:
        new_class = MathClass(section_number)
        new_class.addStudent(0, self.sectionsDict[self.section_numbers[0]].getStudent(0)[1].copy())
        self.section_numbers.append(section_number)
        self.sectionsDict.update({section_number: new_class})
        if file_name:
            sec_num_read = self.readFromFile(file_name)
            return sec_num_read
        
    def saveToFile(self, fileName:str, section_number:int=1):
        # get the file name and the section number, 
        # the file name is to be written to, 
        section = self.sectionsDict[section_number]
        currSectionNames = self.sectionsDict[section_number].getStudentNames()
        currSectionGrades = self.sectionsDict[section_number].getStudentLstGrades()
        with open(fileName, 'w') as f:
            # the section number is the section to write from memory,
            for i in range(len(currSectionNames)):
                    f.write(currSectionNames[i] + ' :\n' + ',\n'.join(currSectionGrades[i])+',\n#\n')
            f.close()
    
    def readFromFile(self, fileName:str, secNum:int=-1):
        with open(fileName, 'r') as f:
            studentName = ''
            studentGrades = []
            for line in f:
                #
                # i want to get the student name and the grades,
                # and then add them to the class,
                # the "#" is used to separate each student, and the "," is used to separate the grades
                if not line.startswith('#'):
                    
                    # check if the line is a student name
                    if line.endswith(':\n'):
                        #
                        # if the line is a student name, strip whitespace and formatting
                        studentName = line.strip(':\n')
                        #
                        # -1 if section number is not specified, attempt to parse the section number from the file
                        if secNum == -1:
                            # get the section number from the first student in the file
                            secNum = int(studentName.split('_')[3])
                            self.section_numbers.remove(-1)
                            self.section_numbers.append(secNum)
                            curCopy = self.sectionsDict.pop(-1)
                            curCopy.sectionNum = secNum
                            self.sectionsDict.update({secNum: curCopy})
                        # get the student id to construct fully qualified name
                        studentID = studentName.split('_')[1]
                    # each grade ends with a comma and a new line, 
                    elif line.endswith(',\n'):# check the condition each line of the file
                        #
                        # if the line is a grade, strip whitespace and formatting, 
                        # then append to the list of grades for THIS STUDENT instance!!!
                        studentGrades.append(line.strip(',\n'))
                # once the student data is compiled, add it to the CORRECT class instance
                elif (studentName != '') and (len(studentGrades) == 4):# 4 is the number of grade categories for each student
                    #
                    # make the student with the relevant name and grades
                    self.sectionsDict[int(secNum)].addStudent(studentID, studentGrades)
                    # reset the student name and grades to compile the next student
                    studentName = ''
                    studentGrades = []
                else:
                    continue
            f.close()
            return secNum
        
    def getSectionDict(self)->'dict[int,MathClass]':
        return self.sectionsDict
    
   
    def showPlot1(self,graphWidth=800, graphHeight=600):
        f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
        axes = f.add_subplot(111)
        for section in self.sectionsDict.values():
            # plot1= x plot2= y and are numpy arrays
            plot1, plot2 = section.getStudentPlot()
            
            # creating pipeline and fitting it on data
            Input=[('polynomial',PolynomialFeatures(degree=5)),('modal',LinearRegression())]
            pipe=Pipeline(Input)
            pipe.fit(plot1.reshape(-1,1), plot2.reshape(-1,1))
            #
            #
            poly_pred=pipe.predict(plot1.reshape(-1,1))
            #sorting predicted values with respect to predictor
            sorted_zip = sorted(zip(plot1,poly_pred))
            x_poly, poly_pred = zip(*sorted_zip)
            print('RMSE for Polynomial Regression=>',numpy.sqrt(mean_squared_error(plot2,poly_pred)))
            #plotting predictions
        
            axes.plot(plot1,plot2,'D')
            # plt.plot(x,y_pred,color='r',label='Linear Regression')
            axes.plot(x_poly,poly_pred,color='g',label='Polynomial Regression')

        axes.set_xlabel("test average")
        axes.set_ylabel("class average")#
        plt.show()
        plt.close('all')