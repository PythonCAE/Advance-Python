from threading import Thread
class Child1(Thread):
    def run(self):
        i = 5
        while(i>0):
            print("Child1 Thread:")
            i -= 1
class Child2(Thread):
    def run(self):
        i = 5
        while(i>0):
            print("Child2 Thread:")
            i -= 1

t1 = Child1()
t2 = Child2()

t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("Main Thread")           