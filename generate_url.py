f=open("./1.txt")
f2=open("./2.txt",mode="w")
for i in f:
    i="https://twitter.com/"+i
    f2.write(i)
    print(i)