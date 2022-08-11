with open("tejas.txt") as f:
    a=f.readlines()
   # a=f.read(7)
    print(a)


f=open("tejas.txt")
print(f.readlines())
print(f.readline())
f.close()