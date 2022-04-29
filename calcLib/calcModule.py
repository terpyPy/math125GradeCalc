#  Author:      Cameron Kerley
#  Date:        04/28/22
try:
    from . import stringHandler
except ImportError:
    import stringHandler
    
def getTestScores(test_total:int, test_taken:int, WEIGHT_FACTOR:float, POINT_WEIGHT:float, depth:int=0)->list:
    # completed_Test_Scores = []
    # separated the 2 loops to make the code more readable
    # this loop prompts the user for the test score of unknown test grade  
    
    # case one is for unknown test grade, bounded to 0 for speculative grade calculations
    if depth == 0:
        
        newScore = (input(f'Enter estimated score for ungraded test #{depth}: '))
        check = stringHandler.intSanityCheck([newScore])
        if check[0] == True:
            newTestPointTot = WeightCalc(WEIGHT_FACTOR, float(newScore))
        else:
            # depth += 1
            return getTestScores(test_total, test_taken, WEIGHT_FACTOR, POINT_WEIGHT, depth)
    
    # get the score in % for each test already taken
     
    Test_Scores = collectGradeData(test_total, test_taken, WEIGHT_FACTOR, POINT_WEIGHT)
                
    return Test_Scores, newTestPointTot

def collectGradeData(test_total, test_taken, WEIGHT_FACTOR, POINT_WEIGHT)->list:
    completed_Test_Scores = []
    # get the score in % for each test already taken  
    for j in range(test_taken):
        print(f'Enter score for test {j+1}')
        score = input()
        cases = stringHandler.intSanityCheck([score])
        if (False in cases):
            return collectGradeData(test_total, test_taken, WEIGHT_FACTOR, POINT_WEIGHT)
        else:
            result = WeightCalc(WEIGHT_FACTOR,float(score))
            completed_Test_Scores.append(result)
            print(f'Expected score for test {j+1} is {result}/{POINT_WEIGHT} :----')
                
    return completed_Test_Scores


def WeightCalc(weight: float, ScoreInPercent)->int:
    # calculate the weight factor for any assignment type
    expected = round((weight * ScoreInPercent),2) 
    return expected
