import argparse
import itertools
import sys
from argparse import ArgumentParser
from enum import Enum
from typing import List, Optional

BOOKS = ["The Last Battle1", "The Screwtape letters", "The Great Divorce"]


class bookState(Enum):
    AVAILABLE = "AVAILABLE"
    RESERVATION = "RESERVATION"
    LENDING = "LENDING"


class Book:
    new_id = itertools.count().__next__

    def __init__(self, name, state: bookState, until_available: int = 0) -> None:
        if not self.__validate(name, state, until_available):
            raise Exception("Validation error in making instance of Book")
        self.id = Book.new_id()
        self.name = name
        self.state = state
        self.until_available = until_available

    def __validate(self, name, state, until_available) -> bool:
        if not isinstance(name, str):
            return False

        if not isinstance(state, bookState):
            return False

        if not isinstance(until_available, int):
            return False

        return True


class Library:
    class Archive:
        def __init__(self, books: List[Book]) -> None:
            self.__book_list = books

        def __find_a_book(self, book_id: int) -> Optional[Book]:
            book = next((x for x in self.__book_list if x.id == book_id), None)
            return book

        def show_available_books(self) -> None:
            print("<Library> Show all available books")
            for book in self.__book_list:
                if book.state == bookState.AVAILABLE:
                    print(f"ID: {book.id}, NAME: {book.name}")
            print("")

        def show_lending_books(self) -> None:
            print("<Library> Show all lend books")
            for book in self.__book_list:
                if book.state == bookState.LENDING:
                    print(f"ID: {book.id}, NAME: {book.name}")
            print("")

        def lend_a_book(self, book_id: int) -> bool:
            book = self.__find_a_book(book_id=book_id)
            if not book:
                print(
                    "<>Library Sorry, the book you have requested is currently not in the library"
                )
                print("")
                return False
            else:
                if book.state == bookState.AVAILABLE:
                    print("<Library> The book you requested has now been borrowed")
                    print("")
                    book.state = bookState.LENDING
                    return True
                else:
                    print(
                        "<Library> Sorry, the book you have requested is not available"
                    )
                    print("")
                    return False

        def add_a_book(self, book_id: int) -> bool:
            book = self.__find_a_book(book_id=book_id)
            if not book:
                print(
                    "<Library> Sorry, the book you tried to return does not belong to the library "
                )
                print("")
                return False
            else:
                if book.state == bookState.LENDING:
                    print("<Library> Thanks for returning your borrowed book")
                    print("")
                    book.state = bookState.AVAILABLE
                    return True
                else:
                    print("<Library> Sorry, that book is not available for borrowing")
                    print("")
                    return False


class User:
    def __init__(self, archive: Library.Archive) -> None:
        self.borrowed_book_list = []
        self.archive = archive

    def request_a_book(self) -> None:
        try:
            book_id = int(input("-> Enter an ID of book you wanna borrow: "))
            ret = self.archive.lend_a_book(book_id=book_id)
            if not ret:
                raise Exception
        except Exception:
            err_msg = "[ERROR] Please enter the correct book ID"
            print(err_msg)

    def return_a_book(self) -> None:
        try:
            self.archive.show_lending_books()
            book_id = int(input("-> Enter an ID of book you wanna return: "))
            ret = self.archive.add_a_book(book_id=book_id)
            if not ret:
                raise Exception
        except Exception:
            err_msg = "[ERROR] Please enter the correct book ID"
            print(err_msg)


def activate_library(archive: Library.Archive):
    user = User(archive=archive)

    main_msg = """
    =====LIBRARY MENU=====
    1. Show all available books
    2. Request a book
    3. Return a book
    4. Exit
    ======================
    """
    print(main_msg)
    err_msg = "[ERROR] Please enter the correct choice"

    while True:
        try:
            choice = int(input("-> Enter a choice: "))
        except Exception:
            print(err_msg)
            continue
        if choice == 1:
            archive.show_available_books()
        elif choice == 2:
            user.request_a_book()
        elif choice == 3:
            user.return_a_book()
        elif choice == 4:
            print("-> Thank you!")
            sys.exit()
        else:
            print(err_msg)


def main():
    parser = ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Please run and initialize along with the list of books",
    )
    parser.add_argument("--books", nargs="*", required=True, help="list of books")
    args = parser.parse_args()
    # print(args.books)
    books = []
    for i in args.books:
        book = Book(name=i, state=bookState.AVAILABLE)
        books.append(book)
    library = Library()
    archive = library.Archive(books=books)
    activate_library(archive=archive)


if __name__ == "__main__":
    main()
