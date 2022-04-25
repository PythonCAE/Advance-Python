# Multi_Level_Inheriatnce:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("My name is"+str(self.name)+" My age is "+ str(self.age))    

class Teacher(Person):
    def __init__(self,name,age,tname):
        super().__init__(name,age)#To call and initialize the its parent class Person
        self.tname=tname

    def show(self):
        print("Teacher name:",self.tname)    
    

class Student(Teacher):
    def __init__(self,name,student_id,gpa,age,tname):
        super().__init__(name,age,tname) #To initialize the Parent class Teacher
        Person.show(self) #To calll the Person's class's show method
        Teacher.show(self) ##To calll the Teacher's class's show method
        self.student_id = student_id
        self.gpa = gpa
    def show(self):
        print("My name is"+(self.name)+" My age is "+ str(self.age)+" My Student_id and gpa are: ",self.student_id,self.gpa)    
       
s=Student("Rupesh Bhujel",1,3,25,"ABC")
s.show()

