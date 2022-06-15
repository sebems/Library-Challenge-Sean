from db_handler import DB_Handler
from student import Student

class STUDENT_DB_Handler( DB_Handler):
    
    def __init__(self):
        self.studDB = DB_Handler("student", "students")
        self.createTable()

    def createTable(self):
        self.studDB.createTable({
            "id" : "integer",
            "fname" : "text",
            "lname" : "text",
            "age" : "integer"
        })

    def insertStudent(self, numOfInputs = 1):
        """
            Inserts n number of entries into table
        """

        for i in range(numOfInputs):
            self.studDB.cursor.execute(" SELECT * FROM students ")
            table_size = len(self.studDB.cursor.fetchall())

            self.studDB.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (table_size + 1, "", "", 0))
        
        self.studDB.conn.commit()

    def getAllStudents(self) -> bool:
        self.studDB.cursor.execute(" SELECT * FROM students ")
        students = self.studDB.cursor.fetchall()
        return students

    def isStudentIn(self, student: Student):
        fName, lName, stud_ID = student.getFirstName(), student.getLastName(), student.id
        
        self.studDB.cursor.execute(" SELECT * FROM students WHERE id= ? AND fname= ? AND lname= ?", (
            stud_ID, fName, lName
        ))

        doesStudentExist = self.studDB.cursor.fetchall()
        return doesStudentExist
        