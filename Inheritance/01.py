class Employee:

    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def language(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmer")
    
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)