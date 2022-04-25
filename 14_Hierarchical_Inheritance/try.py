# Hierachical Inheritance:
class Details:
    def __init__(self,id,name,gender):
        self.__id = id
        self.__name = name
        self.__gender = gender
   
    def showData(self):
        print("Id:",self.__id)
        print("Name:",self.__name)
        print("Name:",self.__gender)

class Employee(Details):
    def __init__(self,id,name,gender,comp,dept):
        super().__init__(id,name,gender)
        self.__company = comp
        self.__dept = dept

    
    def showEmployee(self):
        self.showData()
        print("Company:",self.__company)
        print("Depatment:",self.__dept)


class Developer(Details):
    def __init__(self,id,name,gender,comp,dept):
        super().__init__(id,name,gender)
        self.__comapny = comp
        self.__dept = dept

      

    def showDeveloper(self):
        self.showData()
        print("Company:",self.__comapny)
        print("Depatment:",self.__dept)


def main():
    print("Employee Object")
    e = Employee(1,"Rupesh Bhujel","male","abc","No Role")
    e.showEmployee()
   
    print("Developer Object")
    d = Developer(2,"Rupesh Bhujel1","male","No Comapny","No Role")
    d.showDeveloper()    

if __name__=="__main__":
    main()     




           