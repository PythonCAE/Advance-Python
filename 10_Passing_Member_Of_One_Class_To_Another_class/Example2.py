class Test1:
    def __init__(self):
        self.a=10
        self.b = 15
        self.add=self.a+self.b

    def show(self):
        print("print:",self.add)

class  Test2:
    def show(arg):
        print(arg.show())        

test1 = Test1()
Test2.show(test1)