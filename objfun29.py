#classes are used to define our own data type and class is just like a template and objects are real

class students:

     def __init__(self, name, major,gpa): #init is a fn and name and major are just parameters

       self.name=name #the name of the student object is equal to the name of the name that we passed in
       self.major=major
       self.gpa=gpa


     def on_honor_roll(self):
         if self.gpa >=3.5:
             return True
         else:
             return False