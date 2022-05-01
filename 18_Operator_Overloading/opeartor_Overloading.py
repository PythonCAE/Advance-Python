class A:
    def __init__(self,x):
        self.x =x
    def __add__(self,other):
        sum = self.x + self.other
        return sum    

class B:
    def __init__(self,x):
        self.x =x

a= A(100)
b= B(200)
print(a+b) 

print(10+20)
print(int.__add__(10,20))

      
       
