# math125GradeCalc
student & mathClass classes, provide functionality for studentDataBase.py, makes a searchable database of fake students with unique id numbers, UIDnames, and grade totals. database search is a binary search with a maximum lookup of 20 in 1 mill + students.
  ## UPDATES:
  - version 1.1.0 patch:
    1) over all functionality refactor
    2) streamlined data input, sanity, and class inheritance
    3) encapsulated data retrieval to the proper scope and moved function that manipulate class data to there respective          class method equivalents. 


    ### added:
      1. MathClass.sort method
      2. MathClass.get<gradecategory>Average methods
      3. Sections graphs calculations with RMSE, and plotting
    ### UI:
      - UI events and interaction with MathClass rescoped, top bar menus added
      - Additions: The "New" was tab added
      - Function: adds a new student based on student 0, which is not displayed to the user, and used only as a reference to inti a new student
    ### v1.1.4 UI aaddtions:
      - added: new class sections and new student creation with top menu bar.
      - added: scatter plot funtion for class sections show test avg, class avg relation ship uses RMSE to plot best fit.

![image](https://user-images.githubusercontent.com/66324329/169870478-df57465a-7927-462a-9906-40eb8a64a69a.png)
![image](https://user-images.githubusercontent.com/66324329/169871225-84df091a-3eae-4f91-a220-44aa79ed34cd.png)

# old
added the Student & mathClass classes, provide functionality for studentDataBase.py, makes a searchable database of fake students with unique id numbers, UIDnames, and grade totals. database search is a binary search with a maximum lookup of 20 in 1 mill + students.
  
  # total tests <= 9, all other user inputs can be any valid integer number including negitive floats&ints
  2/4 tests:

  ![image](https://user-images.githubusercontent.com/66324329/165672390-fd16dd9e-8070-4656-bfc5-fa6f964a03fa.png)

  3/4 tests:

  ![image](https://user-images.githubusercontent.com/66324329/165672985-1cfba736-993a-4825-8418-ad8bf2e8a413.png)

