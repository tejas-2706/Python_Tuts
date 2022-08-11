import time
from functools import lru_cache

# @lru_cache(maxsize=3)
# def some_work(n):
#     # some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(2)
#     some_work(9)
#     print("done...again")
#     some_work(3)
#     print("done")


n = int(input("enter maxsize no."))
@lru_cache(maxsize=n)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now running some work")
    some_work(3)
    some_work(1)
    some_work(2)
    some_work(9)
    print("done...again")
    some_work(3)
    print("done")



