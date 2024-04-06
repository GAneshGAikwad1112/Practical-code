class Animal:
    animalType = " Mammal "

class Pets(Animal):
    color = " white "

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Bow Bow!")

d =  Dog()
d.bark()

