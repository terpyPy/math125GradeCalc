
def entryHandler(gradeChosen:str, file_list, idNum, gradeList, window, text):
    # split grade line into list and choose 
    # the first word represents the grade to change
    case = gradeChosen.split(" ")[0]
    caseDict = {"current": file_list.students[int(idNum)].setclassTotal,
                "test": file_list.students[int(idNum)].setTestTotal,
                "class": file_list.students[int(idNum)].setClassWorkTotal,
                "checks": file_list.students[int(idNum)].setCheckAndSetsTotal}
    # if the user entered a grade, change it
    caseDict[case](text)
    gradeList = file_list.getStudent(int(idNum), True)[1]
    window["-student-"].update(gradeList)