class Country:
    def __init__(self,Name,Area,Population):
        self.Name= Name
        self.Area = Area
        self.Population = Population
        
    def show(self):
        print(self.Name,self.Area,self.Population )

class Zone:
    def __init__(self,ZName,District):
        self.ZName = ZName
        self.District = District

    def show(self):
        print(self.ZName,self.District)

class City(Country,Zone):
    def __init__(self,Name,Area,Population,Zname,District,City_Name):
        # super().__init__(Name,Area,Population,Zname,District)
        Country.__init__(self,Name,Area,Population)
        Zone.__init__(self,Zname,District)
        self.City_Name = City_Name 
    def show(self):
         print(self.Name,self.Area,self.Population )
         print(self.ZName,self.District)
         print(self.City_Name)

city =City("Nepal",148181,"3crore","Bagmati","Kathmandu","Dakshinkali")
city.show()         



          
        