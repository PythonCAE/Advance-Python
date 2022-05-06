from abc import ABC,abstractmethod

class Mobile(ABC):
    @abstractmethod
    def price(self):
        pass

    def shape(self):
        print("Rectangular")  
     
class Sony(Mobile):
    def price(self):
        print("20000")

class Samsung(Mobile):
     def price(self):
        print("25000")

so = Sony()
so.shape()
so.price()
print()
sa =  Samsung()
sa.shape()
sa.price()      

