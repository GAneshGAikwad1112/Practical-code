with open("donkey/sample.txt") as f:

    content = f.read()

content = content.replace("donkey","$%@!$^#")


with open('donkey/sample.txt',"w") as f:
    f.write(content)