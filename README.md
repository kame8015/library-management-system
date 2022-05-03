# Library Management System

## Install dependencies

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirement_dev.txt
$ pip install -r requirements.txt
```

## How to run Library Management System

```
$ python app_main.py --books Test1 Test2 Test3

    =====LIBRARY MENU=====
    1. Show all available books
    2. Request a book
    3. Return a book
    4. Exit
    ======================

-> Enter a choice: 1
<Library> Show all available books
ID: 0, NAME: Test1
ID: 1, NAME: Test2
ID: 2, NAME: Test3

-> Enter a choice: 2
-> Enter an ID of book you wanna borrow: 0
<Library> The book you requested has now been borrowed

-> Enter a choice: 1
<Library> Show all available books
ID: 1, NAME: Test2
ID: 2, NAME: Test3

-> Enter a choice: 2
-> Enter an ID of book you wanna borrow: 0
<Library> Sorry, the book you have requested is not available

[ERROR] Please enter the correct book ID
-> Enter a choice: 3
<Library> Show all lend books
ID: 0, NAME: Test1

-> Enter an ID of book you wanna return: 0
<Library> Thanks for returning your borrowed book

-> Enter a choice: 1
<Library> Show all available books
ID: 0, NAME: Test1
ID: 1, NAME: Test2
ID: 2, NAME: Test3

-> Enter a choice: 4
-> Thank you!
```
