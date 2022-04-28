#  Author:      Cameron Kerley
#  Date:        04/03/22
#  Purpose:     Calculate the final grade for a student
# Inputs:       Number of tests taken, number of tests total, score in percent for test
# constants for exam point scale conversion from precents gradeCalc
#  Outputs:     Final grade for student
from calcLib import stringHandler, calcModule
CLASS_WORK_WEIGHT = 25.0
TEST_POINT_WEIGHT = 15.00
CHECKS_AND_SETS_WEIGHT = 15.0


def main()->str:
    # list of prompts for user input
    dataToEnter = stringHandler.promptStrBuilder()
    # do not use last prompt in dataToEnter list
    dataRecived = stringHandler.promptFunctions(dataToEnter, [])
    # unpack list
    testsTotal, testTaken = dataRecived
    # calculate weight factor or total points for class currently, 
    # scales from 0 to 100 based on weight val, ie 3/4 = 100% of class total calculated
    maxScoreTotal = (TEST_POINT_WEIGHT * (testTaken + 1))
    factor = (CHECKS_AND_SETS_WEIGHT + CLASS_WORK_WEIGHT) + maxScoreTotal
    
    print(factor)
    #
    # calculate the weight factors for each assignment type
    EXAM_WEIGHT_FACTOR = TEST_POINT_WEIGHT / factor
    CLASS_WORK_FACTOR = CLASS_WORK_WEIGHT / factor
    CHECKS_AND_SETS_FACTOR = CHECKS_AND_SETS_WEIGHT / factor
    
    print(f'recived:- {testTaken}/{testsTotal} tests taken.')
    
    completedTestScores, newTestPointTot = calcModule.getTestScores(testsTotal, testTaken, EXAM_WEIGHT_FACTOR, TEST_POINT_WEIGHT)
        
                
    x1 = (sum(completedTestScores) + newTestPointTot)
    x2 = calcModule.WeightCalc(CLASS_WORK_FACTOR, float(input(f'Enter % for class work: ')))
    x3 = calcModule.WeightCalc(CHECKS_AND_SETS_FACTOR, float(input(f'Enter % for checks & set\'s work: ')))
    f = round(x1 + x2 + x3,2)
    calcStr = [f'current grade is:--- {f}%',
               f'test point total is:--- {x1}/{maxScoreTotal}',
               f'class work total is:--- {x2}/{CLASS_WORK_WEIGHT}',
               f'checks & sets total is:--- {x3}/{CHECKS_AND_SETS_WEIGHT}']
    calcStr = '\n'.join(calcStr)
    return calcStr
    
           
# if not imported as a module call the data prompt function & execute without saving to file
if __name__ == '__main__':
    run = main()
    print(run)
   