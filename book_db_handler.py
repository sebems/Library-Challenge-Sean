from db_handler import DB_Handler
import random
from book import Book
from typing import List

class BOOK_DB_Handler( DB_Handler ):
    
    def __init__(self):
        self.bookDB = DB_Handler('book', 'books')
        self.createTable()

    def createTable(self):

        self.bookDB.createTable({
            'bookID': 'integer',
            'renter': 'text'
        })

    def updateTable(self, newValue, searchVal):
        """
            Updates the a given table entry
        """

        self.bookDB.cursor.execute(""" UPDATE books 
            SET  renter= ? 
            WHERE bookID= ?
            """, (newValue, searchVal))
        
        self.bookDB.conn.commit()

    def findAllUnRentedBooks(self) -> List:
        """
            Finds all books not checked out and returns sql result
        """
        self.bookDB.cursor.execute(" SELECT * FROM books WHERE renter = ''")
        return self.bookDB.cursor.fetchall()

    def getCurrentBook(self, book_id) -> Book:
        """
            Gets the Current Book Object
        """
        self.bookDB.cursor.execute(""" SELECT * FROM books WHERE bookID = ? """, (book_id,))
        return Book(self.bookDB.cursor.fetchall()[0])

    def insertBook(self, numOfInputs):
        """
            Inserts n number of entries into table
        """

        for i in range(numOfInputs):
            self.bookDB.cursor.execute(" SELECT * FROM books ")
            table_size = len(self.bookDB.cursor.fetchall())
            self.bookDB.cursor.execute("INSERT INTO books VALUES (?, ?)", (table_size + 1, ''))

        self.bookDB.conn.commit()

    def toBookObject(self, sql_result: List[tuple]) -> List[Book]:
        """
            Converts a List of tuples to a list of books
        """
        bookList = []
        for sql_tuple in sql_result:
            bookList.append(Book(sql_tuple))

        return bookList