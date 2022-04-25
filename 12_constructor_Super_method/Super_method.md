# Super Method :
Parent and Child clas have each constructor then child class constructor override to the parent class.

So,Initialization is not in parent class then to solve this problem Super Method is eastablished.

## Way to use:
```python
class Child_Class(Parent_class):
    def __init__(self,parameter):
        super().__init__(parameter)
```

## Example:
```python
class Number:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show1(self):
        print("Value are",self.a,'and',self.b)

class Multiply(Number):
    def __init__(self,a,b,c,d):
        super().__init__(a,b) # Here Parent class constructor is called and argument is passed a and b
        self.c=c
        self.d=d


    def show(self):
        print("sum is:",self.a*self.b)
        print("sum is:",self.c*self.d)

class Add:
    def show(arg): #passing argument as object
        print("Addition is:",arg.a+arg.b)        
mul=Multiply(5,6,8,9)
mul.show()  
mul.show1()                   
Add.show(mul)          
```
## Output:
```
sum is: 30
sum is: 72
Value are 5 and 6
Addition is: 11
```