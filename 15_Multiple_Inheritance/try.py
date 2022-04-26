class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_name_is(self):
        print("My Name is:" +self.name)    

class Athelete:
    def __init__(self,teacher):
        self.teacher = teacher

    def my_name_is(self):
        print("My name is :" + self.teacher)

class Student(Athelete,Person):
    def __init__(self, name, age,student_id,gpa,teacher):
        Person.__init__(self,name,age)
        Athelete.__init__(self,teacher)
        self.gpa =gpa
        self.student_id = student_id
    def my_gpa_is(self):
        print(self.student_id)
        print(self.gpa)


s=Student("Rupesh Bhujuel",25,1,3,"AAA")
s.my_name_is()


                           