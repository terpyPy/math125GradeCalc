from mathClass import MathClass
import matplotlib.pyplot as plt
import numpy 
from scipy.optimize import curve_fit
# TODO: add file IO for this to save to and read from a file
# need to modify the class to be able to read from a file so the constructor 
# needs to be modified to take a file name as a parameter
class Sections(MathClass):
    def __init__(self, fileName=None, math_class:MathClass=None, section_numbers:'list[int]'=[-1]):
        if math_class is not None:
            self.section_numbers = section_numbers
            self.sectionsDict = {self.section_numbers[0]: math_class}
        elif fileName is not None:
            # fileNameContents = fileName.split('/')[-1:]
            # file_sec_num = fileNameContents[0].split('_')[1].split('.')[0]
            
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
    
    def addSection(self, section_number:int=-1, file_name=None):
        new_class = MathClass(section_number)
        new_class.addStudent(0, self.sectionsDict[self.section_numbers[0]].getStudent(0)[1].copy())
        self.section_numbers.append(section_number)
        self.sectionsDict.update({section_number: new_class})
        if file_name:
            sec_num_read = self.readFromFile(file_name)
            return sec_num_read
    
        
    def getSectionDict(self)->'dict[int,MathClass]':
        return self.sectionsDict
    
    def func(self, x, a, b,c):
        # This best fit line is known as regression line,
        # and defined by a linear equation Y= a *X + b.
        return (a * numpy.square(x)) + b * x + c
    
    def saveToFile(self, fileName:str, section_number:int=1):
        # get the file name and the section number, 
        # the file name is to be written to, 
        section = self.sectionsDict[section_number]
        currSectionNames = [section.getStudent(i)[0] for i in range(1,len(section.students))]
        currSectionGrades = [section.getStudent(i)[1] for i in range(1,len(section.students))]
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
        
        
    def showPlot1(self,graphWidth=800, graphHeight=600):
        f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
        axes = f.add_subplot(111)
        for section in self.sectionsDict.values():
            plot1, plot2 = section.getStudentPlot()
            
            axes.plot(plot1, plot2, 'D')
        
            initialParameters = numpy.array([1.0, 1.0, 1.0,])
            fittedParameters, pcov = curve_fit(self.func, plot1, plot2, initialParameters)
            modelPredictions = self.func(plot1, *fittedParameters)
            absError = modelPredictions - plot2
            
            SE = numpy.square(absError) # squared errors
            MSE = numpy.mean(SE) # mean squared errors
            RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
            Rsquared = 1.0 - (numpy.var(absError) / numpy.var(plot2))
            print('RMSE:', RMSE/100)
            print('R-squared:', Rsquared/100)
            
            xModel = numpy.linspace(min(plot1), max(plot1))
            yModel = self.func(xModel, *fittedParameters)
            
            axes.plot(xModel, yModel)

            axes.set_xlabel("class average")
            axes.set_ylabel("test average")#
        plt.show()
        plt.close('all')