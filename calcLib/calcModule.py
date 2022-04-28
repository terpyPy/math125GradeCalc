def getTestScores(test_total, test_taken, WEIGHT_FACTOR, POINT_WEIGHT)->list:
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
                print(f'Expected score for test {j+1} is {result}/{POINT_WEIGHT} :----')
                
    return completed_Test_Scores, newTestPointTot

def WeightCalc(weight: float, ScoreInPercent)->int:
    # calculate the weight factor for any assignment type
    expected = round((weight * ScoreInPercent),2) 
    return expected
