import time
initial=time.time()
j=0
while(j<9):
    print("tejas")
    time.sleep(1)
    j+=1
print("while loop ran in",time.time() - initial,"seconds")

initial2 = time.time()
for i in range(9):
    time.sleep(1)
    print("tejas")
print("for loop ran in", time.time() - initial2,"seconds")

localtime = time.asctime(time.localtime((time.time())))
print(localtime)
