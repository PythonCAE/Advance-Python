# Create a thread by creating a child class to Thread class:

We can create our own thread class by inheriting Thread Class from Threading module.

```
class ChildClassName(Thread)
Thread_object = ChildClassName()
```

# Thread Class's Methods:
* start() - Once a thread is created it should be started by calling start() Method.
* run()-Every thread will run this method and write our own as body of the method.A thread will terminate automatically when it comes out of the run() Method.
* join()- This method is used to wait till teh thread  completely excutes  the run() method.