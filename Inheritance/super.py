class person:
    country = "India"

    def getDetails(self):
        print("hello this is a information function")

    def emp():
        pass
    
    
        
class Employee(person):

    def empSalary(self):
        pass

    def __init__(self):
        super().__init__()
        print(" I AM  a Employee")

p = person()
e = Employee()
e.empSalary()
