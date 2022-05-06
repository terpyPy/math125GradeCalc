#  Author:      Cameron Kerley
#  Date:        04/28/22
#  Description: This function takes a list of inputs and returns a list of data
def getReturnArray(prompt_arr:list, return_arr:list, start_str:str, stop:int=1)->list:
    # for invalid input call self recursively to re-prompt user for data
    for i in range(len(prompt_arr) - stop):
        loop_prompt = start_str + prompt_arr[i]
        return_arr.append(input(loop_prompt))
        
    cases = intSanityCheck(return_arr)
    if (False in cases):
        return getReturnArray(prompt_arr, [], start_str)
    else:
        return return_arr

def promptStrBuilder()->list:
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



def intSanityCheck(caseArr:list)->list:
     # to evaluate if the data recived is valid check if the data is an int
    returnArr = []
    for i in range(len(caseArr)):
        returnArr.append(caseArr[i].isnumeric())
        if returnArr[i] == False:
            try:
                float(caseArr[i].strip('-')) 
                returnArr[i] = True
            except ValueError:
                returnArr[i] = False
                
    return returnArr

def promptFunctions(promptArr: list, returnArr, startStr:str='Please enter ')->list:
    # prompt user for data and return list of data
    # returnArr is list of data recived from user input
    returnArr = getReturnArray(promptArr, returnArr, startStr)
    
    # get the first & second elements of the list 
    testTaken, testsTotal = returnArr[0:2]
    # strip any negative signs from the data not in the domain of the operation
    testTaken = testTaken.strip('-')
    testsTotal = testsTotal.strip('-')
    # 
    # input already validated by getReturnArray, 
    # take only 1-9 values, 10 term exams is unreasonable, cast to int 
    returnArr = [int(testTaken[0]), int(testsTotal[0])]
    return  returnArr

