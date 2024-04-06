#python program to find the largest among three numbers

#using conditional statments

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if (num1>num2) and (num1>num3):
    print(f"The number {num1} is largest")

elif (num2>num1) and (num2>num3):
    print(f"The number {num2} is largest")

else:
     print(f"The number {num3} is largest")