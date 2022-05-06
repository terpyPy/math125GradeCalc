# math125GradeCalc
script for utk math 125 grade speculation
- To use open command prompt and navagite to the dirctory/folder the script is located and type:
- python gradeCalc.py

# UPDATES
- version 1.1.0 patch:
- 1) over all functionality refactor
- 2) streamlined data input, sanity, and class inheritance
- 3) encapsulated data retrieval to the proper scope and moved function that manipulate class data to there respective class method equivalents. 


## added:
-MathClass.sort method
-MathClass.get<gradecategory>Average methods
### UI:
- UI events and interaction with MathClass rescoped, top bar menus added
- 1) New tab added,:
- 2)function, adds a new student based on student 0, which is not displayed to the user, and used only as a reference to inti a new student.
  
![image](https://user-images.githubusercontent.com/66324329/167185086-215fc535-605f-4ded-aeb1-d0d94bace51f.png)
 
# old
added the Student & mathClass classes, provide functionality for studentDataBase.py, makes a searchable database of fake students with unique id numbers, UIDnames, and grade totals. database search is a binary search with a maximum lookup of 20 in 1 mill + students.
  
  # total tests <= 9, all other user inputs can be any valid integer number including negitive floats&ints
  2/4 tests:

  ![image](https://user-images.githubusercontent.com/66324329/165672390-fd16dd9e-8070-4656-bfc5-fa6f964a03fa.png)

  3/4 tests:

  ![image](https://user-images.githubusercontent.com/66324329/165672985-1cfba736-993a-4825-8418-ad8bf2e8a413.png)

