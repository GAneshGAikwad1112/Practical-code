f = open('practic_set/poems.txt')
t = f.read()

if 'twinkel' in t:
    print("Twinkel is present")

else:
    print("Twinkel is not present")

f.close()