from threading import Thread
def disp():
    for i in range(5):
        print("Child thread")

t1 = Thread(target=disp) #until here it is run under main thread
t1.start() #But here new child is start
# From here two main and child are speretly run.
for i in range(5):
    print("Main Thread")

