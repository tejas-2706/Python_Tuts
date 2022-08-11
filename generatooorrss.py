"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
iteration -

"""
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())

for i in g:
    print(i)
h = "Tejas"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for item in h:
#     print(item)


