from typing import List
import sqlite3
from student import Student
from book_db_handler import BOOK_DB_Handler

class BookService:

    def __init__(self) -> None:
        self.dbHandler = BOOK_DB_Handler()

    def find_all(self): 
        return self.dbHandler.findAllBooks()

    def checkout_book(self, book_id: str, student_name: str):
        self.dbHandler.updateTable(student_name, book_id)

if __name__ == "__main__":
    book_service = BookService()
    bookHandler = book_service.dbHandler.bookDB

    book_service.dbHandler.insertBook(3)

    book_service.checkout_book(1, "Joe")
    print(book_service.find_all())

    bookHandler.closeDB()
