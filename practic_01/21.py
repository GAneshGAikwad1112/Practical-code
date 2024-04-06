# Python program to display powers of 2 using anonymous funcrion


nterms = int(input("Enter a number of terms here: "))

result = list(map(lambda x : 2 ** x , range(nterms+1)))

print(result)

for i in range (nterms + 1):
    print("the value of 2 raised to power ",i, "is", result[i])