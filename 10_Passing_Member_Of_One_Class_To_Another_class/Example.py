class Weapon:
    def __init__(self,weapon_name,weapon_damage):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage

    def display_weapon_name(self):
        print('Weapon Name:',self.weapon_name)    

class Person:
    def __init__(self,person_name,health,ranged_weapon):
        self.person_name = person_name
        self.health = health
        self.ranged_weapon = ranged_weapon

    def display_person_info(self):
        print('Name: ' ,self.person_name)
        print('Ranged Weapon :' %Weapon.display_weapon_name)  

    def ranged_attack(self,ranged_weapon,target):
        target.health -= ranged_weapon.weapon_damage
        print("Weapon:",ranged_weapon.weapon_name)
        print(target.person_name+"'s Health:" + str(target.health))

Ak47 = Weapon("Ak47",500)
rup = Person("Rup",100,Ak47) 
rup.display_person_info()      
rup.ranged_attack(Ak47,rup)     
