# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)

def funargs(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    print("\nnowkjsckjs")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
har = ("harry","chole","aashish","bhushan","hinata")
normal = "this is normal argument"
kw={"rohan":"smart","kid":"padahi","muland":"kranti"}
funargs(normal,*har,**kw)

