class Method_Overloading:
    def show(a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!=None:
            s = "Enter the atleast two number"
        else:
            s = "Enter the atleast two number"


        return s
mt = Method_Overloading()
m = mt.show(1)                    
print(m)