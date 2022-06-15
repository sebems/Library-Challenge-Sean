from student_db_handler import STUDENT_DB_Handler
from student import Student

class Student_Service:
    
    def __init__(self) -> None:
        self.dbHandler = STUDENT_DB_Handler()

    def authenticate(self, a_stud: Student):
        self.printMenu(a_stud) if self.dbHandler.isStudentIn(a_stud) else print("No such Student")

    def printMenu(self, a_stud: Student):
        print("Welcome Back " + a_stud.getFirstName())
        print("-------------------------------------\n")

        print("""1. Reserve a Room \n
                 2. Rent Out a Book \n
                 3. Logout
              """)

        # TODO: get input from user