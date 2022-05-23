from mathClass import MathClass
import matplotlib.pyplot as plt
import numpy 
from scipy.optimize import curve_fit
class Sections(MathClass):
    def __init__(self, math_class:MathClass, section_numbers:'list[int]'):
        self.section_numbers = section_numbers
        self.sectionsDict = {self.section_numbers[0]: math_class}
        
    def addSection(self, section_number:int):
        new_class = MathClass(section_number)
        new_class.addStudent(0, self.sectionsDict[self.section_numbers[0]].getStudent(0)[1].copy())
        self.section_numbers.append(section_number)
        self.sectionsDict.update({section_number: new_class})
    
        
    def getSectionDict(self)->'dict[int,MathClass]':
        return self.sectionsDict
    
    def func(self, x, a, b,c):
        # This best fit line is known as regression line,
        # and defined by a linear equation Y= a *X + b.
        return (a * numpy.square(x)) + b * x + c
       
        
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