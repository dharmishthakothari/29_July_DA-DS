with open('FileWrite.txt',"a") as f:
    while True:
        data=input("Enter data to write into file ")
        #if data=="END" or data=="end":
        if data in ("END","end","EXIT","exit"):
            break
        f.write(data)    