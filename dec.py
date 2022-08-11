# def function1():
#     print("subscribe now")
#
# func2 = function1
# del function1
# func2()

# def function1(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = function1(1)
# print(a)

# def executor(func):
#     func("thiss")
#
# executor(print)

def dec1(func1):
    def nowexecute():
       print("executing now")
       func1()
       print("executed")
    return nowexecute
@dec1
def who_is_tejas():
    print("he is a good boy")

# who_is_tejas = dec1(who_is_tejas)
who_is_tejas()