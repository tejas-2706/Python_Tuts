
# -----------------map---------------
# numbers = ["3","45","67"]
# numbers = list(map(int, numbers))
# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2]+1
# # print(numbers[2])

# def sq(a):
#     return a*a
# num =[2,4,5,3,6,7,8]
# square = list(map(sq, num))
# print(square)


# num =[2,4,5,3,6,7,8]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# function = [square,cube]
# # num =[2,4,5,3,6,7,8]
# for i in range(5):
#     val = list(map(lambda x:x(i), function))
#     print(val)

# -----------------filter---------------
# list1 = [3,5,3,6,7,7,7,5,4,3,76,4]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5,list1))
# print(gr_than_5)

# -----------------reduce---------------
from functools import reduce
list2 = [4,5,3,7,8,9]
num = reduce(lambda x,y:x*y, list2)
# num = 0
# for i in list2:
#     num = num+i
print(num)