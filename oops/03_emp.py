class Employee:
    company = "Google"
    salary = 100
    address = "Pune"

harry = Employee()
rajani = Employee()
ganesh = Employee()

harry.salary = 300
rajani.salary = 400

print(harry.company)
print(harry.company)

Employee.company = "Youtube"

print(harry.company)
print(rajani.company)

print(harry.salary)
print(rajani.salary)
print(ganesh.salary)
print(ganesh.address)