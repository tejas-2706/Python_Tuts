# create a library class
# display book
# lend book
# add book
# return book
# JNEC_Library = Library(listofbooks, library_name)

# dictionary (books = keys,value = name of person)

# create a main function and then run it to a infinite
# while loop asking users for their input like:-
# - To display all books
# - To display all available books
# - lend the book                                                           update,pop,append
# - return the book


# class jnec_library:
#     def __init__(self, list_books, borrowers_dict):
#         self.list_books = list_books
#         self.borrowers_dict = borrowers_dict
#
#     def display_books(self):
#         print("This are the following books at Library:-")
#         for book in self.list_books:
#             print(book)
#
#     def lend_book(self, book, borrower):
#         self.book = book
#         self.borrower = borrower
#         if book not in self.borrowers_dict:
#             borrowers_dict.update({book:borrower})
#             print("lender-book databse updated succesfully!!")
#         else:
#             print("Book is already issued to "+self.borrowers_dict[book])
#
#     def add_book(self, book):
#         self.list_books.append(book)
#         print("Book has been added to the book list")
#
#     def return_book(self):
#         self.lend_book.remove(book)
#
# if __name__ == '__main__':













# list_books =["harry potter","jerry","engineering physics"]
# book = input("Enter book name:")
# borrower = input("Enter borrowers name:")
# borrowers_dict = {}
# library = jnec_library(list_books,borrowers_dict)
# library.display_books()
# library.lend_book(book,borrower)
# library.borrowers_dict(book,borrower)


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],
                    "CodeWithHarry")

    while (True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue


