#  Author:      Cameron Kerley
#  Date:        04/03/22
#  Purpose:     Calculate the final grade for a student
# Inputs:       Number of tests taken, number of tests total, score in percent for test
# constants for exam point scale conversion from precents gradeCalc
from cgitb import reset
from unittest import result


CLASS_WORK_WEIGHT = 25.0
TEST_POINT_WEIGHT = 15.00
CHECKS_AND_SETS_WEIGHT = 15.0

def getReturnArray(prompt_arr:list, return_arr:list, start_str:str)->list:
    for i in range(len(prompt_arr) - 1):
        loop_prompt = start_str + prompt_arr[i]
        return_arr.append(input(loop_prompt))
    return return_arr

def promptFunctions(promptArr: list, returnArr, startStr:str='Please enter ')->list:
    # prompt user for data and return list of data
    # promptArr is list of prompts for user input
    # returnArr is list of data recived from user input
    returnArr = getReturnArray(promptArr, returnArr, startStr)
    
    # get the first & second elements of the list 
    testTaken, testsTotal = returnArr[0:2]
    # to evaluate if the data recived is valid check if the data is an int
    cases = [testTaken.isnumeric(), testsTotal.isnumeric()]
    
    # for invalid input call self recursively
    if (False in cases):
        startIndex = cases.index(False)
        msg = 'Please enter an integer for'
        if startIndex == 0:
            print(f'{msg} {promptArr[startIndex]}\n')
        else:
            print(f'{msg} {promptArr[startIndex+1]}\n')
        return promptFunctions(promptArr, [], startStr)
        
    # only return values if all inputs are valid 
    elif (cases == [True, True]):
        returnArr = [int(testTaken), int(testsTotal)]
        return  returnArr

def getTestScores(test_total, test_taken, WEIGHT_FACTOR)->list:
    completed_Test_Scores = []
    for i in range(test_total - test_taken):
        if i == 0:
            newScore = int(input(f'Enter estimated score for ungraded test #{i}: '))
            newTestPointTot = WeightCalc(WEIGHT_FACTOR, newScore)
            for j in range(test_taken):
                print(f'Enter score for test {j+1}')
                score = input()
                result = WeightCalc(WEIGHT_FACTOR,float(score))
                completed_Test_Scores.append(result)
                print(f'Expected score for test {j+1} is {result}/{TEST_POINT_WEIGHT} :----')
                
    return completed_Test_Scores, newTestPointTot

def WeightCalc(weight: float, ScoreInPercent)->int:
    
    expected = round((weight * ScoreInPercent),2) 
    return expected

def propmtStrBuilder()->list:
    # build prompt string
    result = []
    startStr = 'number of tests' 
    midStr_Case1 = 'overall'
    midStr_Case2 = 'taken'
    endStr = 'this semester: '
    startEndArr = [startStr, endStr]
    midArr = [midStr_Case1, midStr_Case2]
    for i in range(len(midArr)):
        result.append(f'{startEndArr[0]} {midArr[i]} {startEndArr[1]}')
    result.append('score in percent for test: ')
    return result

def main()->str:
    # list of prompts for user input
    dataToEnter = propmtStrBuilder()
    # do not use last prompt in dataToEnter list
    dataRecived = promptFunctions(dataToEnter, [])
    # unpack list
    testsTotal, testTaken = dataRecived
    # calculate weight factor or total points for class currently, 
    # scales from 0 to 100 based on weight val, ie 3/4 = 100% of class total calculated
    factor = (CHECKS_AND_SETS_WEIGHT + CLASS_WORK_WEIGHT) + (TEST_POINT_WEIGHT * (testTaken + 1))
    
    print(factor)
    #
    # calculate the weight factors for each assignment type
    EXAM_WEIGHT_FACTOR = TEST_POINT_WEIGHT / factor
    CLASS_WORK_FACTOR = CLASS_WORK_WEIGHT / factor
    CHECKS_AND_SETS_FACTOR = CHECKS_AND_SETS_WEIGHT / factor
    
    print(f'recived:- {testTaken}/{testsTotal} tests taken.')
    
    completedTestScores, newTestPointTot = getTestScores(testsTotal, testTaken, EXAM_WEIGHT_FACTOR)
        
                
    x1 = round((sum(completedTestScores) + newTestPointTot),2)
    x2 = WeightCalc(CLASS_WORK_FACTOR, float(input(f'Enter % for class work: ')))
    x3 = WeightCalc(CHECKS_AND_SETS_FACTOR, float(input(f'Enter % for checks & set\'s work: ')))
    f = x1 + x2 + x3
    return f'current grade is:--- {f}%'
    
           
# if not imported as a module call the data prompt function & execute without saving to file
if __name__ == '__main__':
    run = main()
    print(run)
   