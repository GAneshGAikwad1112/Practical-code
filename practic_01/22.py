# Python program to find numbers divisible by another number

print("The numbers divisible by 13 are: ")
for i in range (1, 100):
    if i % 13 == 0:
        print(i)



#solution 2

l = [39, 48, 26, 98, 33, 67, 87]

result =list(filter(lambda x : x % 13 == 0, l))

print(result)