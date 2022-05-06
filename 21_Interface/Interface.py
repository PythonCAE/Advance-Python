from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        pass

class Child(Father):
    def display(self):
        print("Child Class")

class GradChild(Child):
    def show(self):
        print("GarndChild Class:")


child=Child()
child.display()   
grand =GradChild()
grand.display()
grand.show()
