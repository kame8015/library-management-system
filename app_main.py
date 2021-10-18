import sys


class Library:
    def __init__(self, list_books: list):
        self.availability_books = list_books

    def sort_availability_books(self):
        self.availability_books.sort()

    def lend_book(self, request_book: str):
        print("")
        if request_book in self.availability_books:
            print("The book you requested has now been borrowed")
            self.availability_books.remove(request_book)
        else:
            print("Sorry the book you have requested is currently not in the library")

    def add_book(self, return_book):
        if not return_book in self.availability_books:
            self.availability_books.append(return_book)
            print("")
            print("Thanks for returning your borrowed book")
        else:
            print("")
            print("Sorry the book you have returned is currently in the library")

    # def add_to_temp(self, return_book: str):
    #     print("")
    #     if not self.availability_books:
    #         self.availability_books.remove(return_book)
    #         print("Added to temporary")

    # def add_from_temp(self, ):
    #     print("")
    #     if


# class TemporaryLibrary:
#     def __init__(self, list_books: list):
#         self.reserved_books = list_books

#     def remove(self, request):
#         if request in self.reserved_books:
#             self.reserved_books.remove(request)

#     def add(self, request):
#         if not request in self.reserved_books:
#             self.reserved_books.append(request)


class Student:
    def request_book(self):
        print("")
        print("Enter the name of the book you'd like to borrow>>")
        self.book = input()
        return self.book

    def return_book(self):
        print("")
        print("Enter the name of the book you'd like to return>>")
        self.book = input()
        return self.book


def main():
    BOOKS = ["The Last Battle1", "The Screwtape letters", "The Great Divorce"]
    library = Library(BOOKS)
    student = Student()
    print(
        "=====LIBRARY MENU=====\n"
        + "1. Request a book\n"
        + "2. Return a book\n"
        + "3. Exit\n"
        + "======================"
    )
    while True:
        print("")
        print("-----The books in library-----")
        library.sort_availability_books()  # sort by name
        books = library.availability_books
        for book in books:
            print(book)
        print("------------------------------")
        print("")

        try:
            choice = int(input("Enter Choice: "))
        except Exception:
            print("[ERROR] Please enter the correct choice")
            continue
        if choice == 1:
            library.lend_book(student.request_book())
        elif choice == 2:
            library.add_book(student.return_book())
        elif choice == 3:
            print("Bye")
            sys.exit()
        else:
            print("[ERROR] Please enter the correct choice")
            print("")


if __name__ == "__main__":
    main()
