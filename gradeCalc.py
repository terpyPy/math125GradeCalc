#  Author:      Cameron Kerley
#  Date:        04/03/22
#  Purpose:     Calculate the final grade for a student
# Inputs:       Number of tests taken, number of tests total, score in percent for test
# constants for exam point scale conversion from precents gradeCalc
CLASS_WORK_WEIGHT = 25.0
TEST_POINT_WEIGHT = 15.00
CHECKS_AND_SETS_WEIGHT = 15.0


def promptFunctions(promptArr: list, returnArr, startStr:str='Please enter ')->list:
    # if startIndex not None get a list of values from startIndex to end of promptArr
    # when passed 0 both prompts received none integer values
    # if startIndex != None:
    #     promptArr = promptArr[startIndex:]
    #     startIndex = None
    
    for i in range( len(promptArr) - 1):
        loopPrompt = startStr + promptArr[i]
        returnArr.append(input(loopPrompt))
        
    testTaken, testsTotal = returnArr[0:2]
    cases = [testTaken.isnumeric(), testsTotal.isnumeric()]
    
    # for invalid input call self recursively
    if (False in cases):
        startIndex = cases.index(False)
        if startIndex == 0:
            print(f'Please enter an integer for {promptArr[startIndex]}\n')
        else:
            print(f'Please enter an integer for {promptArr[startIndex+1]}\n')
        return promptFunctions(promptArr, [], startStr)
        
        

    # only return values if all inputs are valid 
    elif (cases == [True, True]):
        returnArr = [int(testTaken), int(testsTotal)]
        return  returnArr

def promptUserForData()->str:
    # list of prompts for user input
    dataToEnter = ['number of test this semester: ', 'number of tests taken this semester:  ', 'score in percent for test: ']
    # do not use last prompt in dataToEnter list
    dataRecived = promptFunctions(dataToEnter, [])
  
    testsTotal, testTaken = dataRecived
    
    # cases for the factor of point scale based on num of tests taken
    if testTaken == 3:
        factor = 100.00
    elif testTaken == 2:
        factor = 85.00
    # default case quits program
    else:
        return
    
    EXAM_WEIGHT_FACTOR = TEST_POINT_WEIGHT / factor
    CLASS_WORK_FACTOR = CLASS_WORK_WEIGHT / factor
    CHECKS_AND_SETS_FACTOR = CHECKS_AND_SETS_WEIGHT / factor
    completedTestScores = []
    print(f'recived:- {testTaken}/{testsTotal} tests taken.')
    for i in range(testsTotal - testTaken):
        if i == 0:
            newScore = int(input(f'Enter estimated score for ungraded test #{i}: '))
            newTestPointTot = WeightCalc(EXAM_WEIGHT_FACTOR, newScore)
            for j in range(testTaken):
                print(f'Enter score for test {j+1}')
                score = input()
                result = WeightCalc(EXAM_WEIGHT_FACTOR,float(score))
                completedTestScores.append(result)
                print(f'Expected score for test {j+1} is {result}/{TEST_POINT_WEIGHT} :----')
        
                
    x1 = round((sum(completedTestScores) + newTestPointTot),2)
    x2 = WeightCalc(CLASS_WORK_FACTOR, float(input(f'Enter % for class work: ')))
    x3 = WeightCalc(CHECKS_AND_SETS_FACTOR, float(input(f'Enter % for checks & set\'s work: ')))
    f = x1 + x2 + x3
    print(f'current grade is:--- {f}')
    #todo figure out the actual grad scale
        

def WeightCalc(weight: float, ScoreInPercent)->int:
    
    expected = round((weight * ScoreInPercent),2) 
    return expected

# if not imported as a module call the data prompt function & execute without saving to file
if __name__ == '__main__':
    run = promptUserForData()
   