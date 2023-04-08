#Create a python function that calculate the age of student, if the student 
# age is greater than or equal to 18 it should return true else false


import datetime


def student_age():
    # student are allowed to input their names
    birth_year = int(input("enter yuor birth year: "))
    # calculation of curent year using datetime module
    current_year = datetime.datetime.now().year
  
    age = current_year - birth_year
    if age >= 18:

      print(bool(age))
    else:
       print(bool())
      
    
student_age()
