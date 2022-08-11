# Diamond shape problem in multiple inheritance

class A:
    def met(self):
        print("I am from class A")
class B(A):
    def met(self):
        print("I am from class B")
class C(A):
    def met(self):
        print("I am from class C")
class D(B, C):
    def met(self):
        print("I am from class D")

a = A()
b = B()
c = C()
d = D()

d.met()