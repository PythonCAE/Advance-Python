class Number:
    def __init__(self):
        print("Main Class")
    def show1(self):
        print("Main class1")    

class Number2(Number):
    def __init__(self):
        super().__init__()
        print("Second main class")
    def show2(self):
        print("Main class2")    
    

class Number3(Number2):
    def __init__(self):
        super().__init__()
        print("Third main class:")
    def function(self):
        print("MultiLevel Inheritance")
n=Number3()
# n.show1()
# n.show2()
# n.function()


     