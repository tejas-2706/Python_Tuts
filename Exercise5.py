# Health Management System
# clients - Harry, Rohan and Hammad
def gettime():
    import datetime
    return datetime.datetime.now()
# Total 6 files
# write a function that when executed takes as input client name

# f=open("Harry food logs")
# print(f.readlines())

# A programm when executed should ask whoes file to be executed with input as name then, for food logs
# using (1,2) and same for exercise logs(1,2)
log_ret=int(input("Mention 1 for log & 2 for retrieve:"))
client_name = int(input("Mention client name by 1 for Harry,2 for Rohan & 3 for Hammad:"))
if log_ret==1:
    if client_name == 1:
        a = int(input("Mention 1 for Harry food logs or 2 for Harry Exercise logs:"))
        if a == 1:
            f=open("Harry food logs","a")
            data=input("Enter Harry's food eaten:")
            print(f.write("\n"+str([str(gettime())]) + "  " + data ))
            f.close()
            print("Succesfully written!!")
        else :
             f=open("Harry Exercise logs","a")
             data=input("Enter Exercise name:")
             print(f.write("\n"+str([str(gettime())]) + " " + data))
             f.close()
             print("Succesfully written!!")
    elif client_name == 2:
        b = int(input("Mention 1 for Rohan food logs or 2 for Rohan Exercise logs:"))
        if b == 1:
             f = open("Rohan food logs","a")
             data=input("Enter Rohan's food eaten:")
             print(f.write("\n"+str([str(gettime())]) + " " + data))
             f.close()
             print("Succesfully written!!")
        else :
             f = open("Rohan Exercise logs","a")
             data=input("Enter Exercise name:")
             print(f.write("\n"+str([str(gettime())])+" "+data))
             f.close()
             print("Succesfully written!!")
    elif client_name == 3:
        if c == 1:
            c = int(input("Mention 1 for Hammad food logs or 2 for Hammad Exercise logs:"))
            f = open("Hammad food logs","a")
            data = input("Enter Hammad's food eaten:")
            print(f.write("\n"+str([str(gettime())]) + " " + data))
            f.close()
            print("Succesfully written!!")
        else:
            f = open("Hammad Exercise logs","a")
            data = input("Enter Exercise name:")
            print(f.write("\n" + str([str(gettime())]) + " " + data))
            f.close()
            print("Succesfully written!!")
    else:
        print("ERROR!!")
elif log_ret==2:
    if client_name == 1:
        d = int(input("Mention 1 for Harry food log or 2 for Harry Exercise log:"))
        if d==1:
            f = open("Harry food logs")
            print(f.read())
            f.close()
        else:
            f = open("Harry Exercise logs")
            print(f.read())
            f.close()
    elif client_name == 2:
        e = int(input("Mention 1 for Rohan food log or 2 for Rohan Exercise log:"))
        if e==1:
            f = open("Rohan food logs")
            print(f.read())
            f.close()
        else:
            f = open("Rohan Exercise logs")
            print(f.read())
            f.close()
    elif client_name == 3:
        g = int(input("Mention 1 for Hammad food log or 2 for Hammad Exercise log:"))
        if g==3:
            f = open("Hammad food logs")
            print(f.read())
            f.close()
        else:
            f = open("Hammad Exercise logs")
            print(f.read())
            f.close()
else :
    print("Error")



