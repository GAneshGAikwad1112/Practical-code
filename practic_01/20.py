# Python program to find the sum of natural number 

num = int(input("Enter a num: "))

if num<0:
    print("enter a positive number!")

else:
    sum = 0
    while num>0:
        sum += num
        num -= 1
    
    print(sum)