# Abstract Class:
A class derived from ABC class which belongs to abc module,is known as abstract class in python.

ABC Class is known as Meta Class which means a class that defines the behavior of other classes.So we can say,meta Class ABC defines that the class which is derived from it becomes an abstract class.



Abstract Class can have abstract method and concrete methods.

Abstract Class needs to be extended and its method implemented.(It is needed to inheriate Abstarct,it means Abstract must have child class. )

PVM can not create objects of an abstract class.



EX:-

```python
from abc import ABC,abstractmethod
class Father(ABC):

```


 ## Abstract Method:
A abstract method is a method whose action is redefined in the child classes as per the requirement of the object.

We can declare a method as abstract method by using @abstractmethod decorator.

Abstract method is method without body


Ex:-

``` python
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

```

 ## Concrete Method:
A concrete method is a method whose action is defined in the abstract class itself.

Concrete method is method with body


Ex:-
``` python
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete Method")
```

## Rules:

* PVM can not create objects of an abstract class.
* It is not necessary to declare all methods abstract in a abstract class.
* Abstract Class can have abstract method and concrete methods.   
* If there is any abstract method in a class, that class must be abstract.
  For example:
  ```python
  class Father(ABC):
      def disp(self,p1...pn):
          pass
  ```
  It must ABC class means child class must be inheriate from ABC class.
* The abstract methods of an abstract class must be defined in its childclass/subclass.
* If you are inheriting any abstract class that have abastract method,you must either provide the implementation of the method or make this class abstract.

## When  use Abstract Class:
We use abstract class when there are some common feature shared by all the objects.      

