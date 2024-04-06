
#use open function for reading the data from the file

f = open('sample.txt','r') 

data = f.read()

print(data)

f.close()