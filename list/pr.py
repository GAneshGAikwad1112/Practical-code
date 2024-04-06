words = ['donkey', 'kaddu']

with open('list/sample.txt')as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^$^#")

with open('list/sample.txt','w') as f:
    f.write(content)