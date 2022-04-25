class Number:
    def __init__(self):
       self.a = 5
       self.b = 6

    def show1(self):
        print("Sum of Parent Class is:"+ str(self.a+self.b))    
   

class Multiply(Number): #Class Multiply extends the property of the base class Number.
    def __init__(self,c,d):
        self.c = c
        self.d = d
    def show(self):
        print("Sum of Child Class:"+str(self.c+self.d))

class Subtract(Number):
    def show(self):
        print(self.a)       
m=Multiply(5,3)
s=Subtract()
m.show()  
s.show1()
s.show()
