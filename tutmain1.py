import sklearn

def printhar(string):
    return f"take this string{string}"

def add(n1,n2):
    return n1+n2+5

print(f"and the name is {__name__}")
if __name__ == '__main__':
    print(printhar("tejas"))
    a = add(7,7)
    print(a)