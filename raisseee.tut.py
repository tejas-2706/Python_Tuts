# a = input("What is your name")
# b = input("How much do you earn")
# if int(b) == 0:
#     raise ZeroDivisionError("b is zero, so stopping the  program")
# if a.isnumeric():
#     raise Exception("no. not allowed")
#
# print(f"{a},how are you?")

c = input("kya he tera nam?")
try:
    print(a)

except Exception as e:
    if c == "tejas":
        raise ValueError("You are blocked")

    print("exceptional handled")




























