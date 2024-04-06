with open("log/log.txt")as f:

    content = f.read()

if 'python' in content.lower():
    print ("Yes python is in the content")

else:

    print("python is not present")