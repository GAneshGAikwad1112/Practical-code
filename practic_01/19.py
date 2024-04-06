# Python program to check Armstrong number in a interval


Lower = int(input("Enter a Lower limit: "))
Upper = int(input("Enter a Upper limit: "))


for num in range (Lower, Upper + 1):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0  :
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num :
        print(num)