# def searcher():
#     import time
#     book = "Treasurey is the key to " \
#            "find the gold" \
#            " and diamonds "
#     time.sleep(3)
#
#     while True:
#         text = (yield)    #generate the value on the way
#         if text in book:
#             print("Text is in your book")
#         else:
#             print("Text is not in your book")
# search = searcher()
# print("searching started")
# next(search)
# search.send("and")
# input("press key")
# search.send("Treasurey")
#
# search.close()
# search.send("treasure ")


# book = ["tejas", "Arjun", "Aum",
#         "Ishan", "Krish", "Rishi",
#         "Veer"]




def searcher():
    import time
    book = "tejas Arjun Aum Ishan Krish Rishi Veer"
    time.sleep(3)

    while True:
        text = (yield)    #generate the value on the way
        if text in book:
            print("Name is in the file")
        else:
            print("Name is not in the file")
search = searcher()
print("searching started")
next(search)
search.send("Veer")



































