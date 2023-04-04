import datetime

def student_age():
    birth_year = int(input("enter yuor birth year: "))
    current_year = datetime.datetime.now().year

    age = current_year - birth_year
    if age >= 18:

      print(bool(age))
    else:
       print(bool())
      
    
student_age()



