class Number:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show1(self):
        print("Value are",self.a,'and',self.b)

class Multiply(Number):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d


    def show(self):
        print("sum is:",self.a*self.b)
        print("sum is:",self.c*self.d)



class Add:
    def show(arg):
        print("Addition is:",arg.a+arg.b)        
mul=Multiply(5,6,8,9)
mul.show()  
mul.show1()                   
Add.show(mul)