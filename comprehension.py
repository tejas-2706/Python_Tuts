# ls = []
# for i in range(50):
#     if i%3==0:
#         if i%3==0:
#             ls.append(i)
# print(ls)
#
# ls = [i for i in range(100) if i%3==0]
# print(ls)

# d1 = {i:f"item {i}" for i in range(10) if i%3==0}
# d2 = {value:key for key,value in d1.items()}
# print(d1,"\n",d2)

# dresses = {dress for dress in ["d1","d2","d2"]}
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

for i in evens:
    print(i)
# Q)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# how many items do you want to put
# then run an for loop
# list as a input
# what type of compression:
# 1)list
# 2)dictionary
# 3)set
# print that compressionn



jgv








