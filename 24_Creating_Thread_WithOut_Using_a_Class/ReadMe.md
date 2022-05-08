# Creating a Thread:
* Thread class of threading module is used to create threads.
* To create our own thread we need to create an object of Thread Class.
* Following are the ways of creating threads:-
    * Creating a thread without using a class
    * Creating a thread by creating a child class to Thread class.
    * Creating a thread without creating child class to Thread class.

# creating a thread without using a class:
```python
from threading import Thread
thread_object = Thread(target = function_name,args=(arg1,arg2,....))
thread_object - It represents our Thread
target - It represent teh function on which the thread will act.
args - It represent a tuple of arguments which are passed to the function.
```
## Example:
```python
t = Thread(target=disp,args=(10,20))

```

# How to Start Thread:
Once a Thread is created it should be started by calling start() Method.

```python
from threading import Thread
def disp(a,b):
    print("The sum is:",a+b)
t1 = Thread(target= disp,args =(10,20))
t1.start()    
```
