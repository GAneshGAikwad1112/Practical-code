class Employee:
    company = "Visa"
    ecode = 120

class Freelanser:
    company = "fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelanser):
    name = "Ganesh"

p = Programmer()
p.upgradeLevel()
print(p.company)
print(p.level)