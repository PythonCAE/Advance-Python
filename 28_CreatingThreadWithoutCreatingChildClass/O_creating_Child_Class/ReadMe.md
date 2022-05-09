# Create a thread w/o creating a child class to Thread Class:

We can create an independent thread child class that does not inherit from Thread Class from threading module.
 ```
 class ClassName:
       statement
object_name = ClassName()
Thread_Object = Thread(target = object_name.function_name,args = (arg1,arg2...))       
 ```

 ```python
 class Mythread:
     def disp(self,a,b):

myt = Mythread()

t = Thread(traget=myt.disp,args=(10,20))
t.strat()


 ```