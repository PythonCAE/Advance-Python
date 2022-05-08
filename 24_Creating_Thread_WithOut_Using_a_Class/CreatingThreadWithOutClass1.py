from threading import Thread
def disp(a,b):
    print("sum is:",a+b)

t1 = Thread(target=disp,args=(10,20))
t1.start()    