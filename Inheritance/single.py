class Employee:

    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    #company = "Youtube"

    def getlanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmer")
    
e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
