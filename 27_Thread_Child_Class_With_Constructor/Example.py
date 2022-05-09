from threading import Thread
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Thread Constructor")

t = MyThread()
t.start()
print("Main Thread")        

