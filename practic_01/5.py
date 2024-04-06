#solution using 3rd variable

a = 15
b = 22
 
temp = a
print("The value of temp variable is ", temp)
a = b
print("The value of a variable is ", a)
b = temp
print("The value of b variable is ", b)

print("value of a and b is ", a , b)


#solution using left and right

a = 12
b = 23

a, b = b, a

print("The values of a and b is ", a, b)