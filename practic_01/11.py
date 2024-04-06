#Python program to check prime number

num = int(input("Enter a number: "))

if num == 1:
    print(f"{num} is not prime number")

if num > 1:

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is a not prime number")
            break
    else:
        print(f"{num} is a prime number")