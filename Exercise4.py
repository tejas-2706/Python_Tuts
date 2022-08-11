# Question of Exercise 4
# Pattern Printing
# Input = Integer n i.e input no.
# Boolean = True or False ; true=1 and false=0

# True n=4
# *
# **
# ***
# ****
#
# False n=4
# ****
# ***
# **
# *

print("enter no. of rows")
rows = int(input())
print("mention 1 for increasing order or 0 for decreasing")
a = int(input())
if a == 1:
    for i in range(0,rows+1):
        print("*"*i)

elif a == 0:
    for i in range( rows,0,-1):
        print("*"*i)
