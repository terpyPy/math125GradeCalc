def getReturnArray(prompt_arr:list, return_arr:list, start_str:str, stop:int=1)->list:
    for i in range(len(prompt_arr) - stop):
        loop_prompt = start_str + prompt_arr[i]
        return_arr.append(input(loop_prompt))
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
            print(f'------- :{msg} {promptArr[startIndex]}-------\n')
        else:
            print(f'------- :{msg} {promptArr[startIndex+1]}-------\n')
        return promptFunctions(promptArr, [], startStr)
        
    # only return values if all inputs are valid 
    elif (cases == [True, True]):
        returnArr = [int(testTaken), int(testsTotal)]
        return  returnArr