# Python program to find the factorial of a number

num = int(input("Enter a Num: "))

fact = 1

if num < 0 :
    print("factorial of 0 does not exist")

if num == 0:
    print("factorial of 0 is ",1)

if num > 0:

    for i in range(1, num+1):
        fact = fact + i 
print("factorial of the given number is ",fact)



# Python program to find the factorial of a number using recursion

num = int(input("Enter a Num: "))


def fact(num):
    if num == 0 :
        return 1
    
    else:
        return ((num) * (fact(num-1)))
    
result = fact ( num )

print(result)