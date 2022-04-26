class Method_OverLoading:
    # def __init__(self,a,b,c) :
    #     self.a =a
    #     self.b = b
    #     self.c = c

    def show(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s="Enter at least Two Number: "
        return s             
def main():
    mo = Method_OverLoading()
    n=mo.show(5,7,6)
    n=mo.show(5,7)
    n=mo.show()
    print(n)
    

if __name__ == '__main__':
    main()
            
       