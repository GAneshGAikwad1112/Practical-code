content =True
i=1
with open("log/log.txt")as f:
   
    while content:
        content = f.readline()
      
        if 'python' in content.lower():
            
            print(content)
            print ("Yes python is in the content")
            print(i)

        i+=1
        