from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete Method")

class Son(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

s = Son()
s.disp()
s.show()         