# Python program to display fibonacci sequence

a = 0
b = 1
n = 7

if n == 1:
    print(a)

else:
    print(a)
    print(b)

    for i in range (1, n+1):
        c = a + b
        a = b
        b = c

        print(c)
