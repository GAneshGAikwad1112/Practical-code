a = int (input("Enter a first number: "))
b = int (input("Enter a second number: "))
class sum:

    def __sum__(self, a, b):
        self.a = a
        self.b = b

c = sum()
print(f"sum of the {a} and {b} is {a+b}")