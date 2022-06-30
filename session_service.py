from student_service import Student_Service
from student import Student

class SessionService: 

    def __init__(self) -> None:
        pass

    def log_in(name: str) -> bool:
        stud = Student("John", "Doe")
        student_service = Student_Service()
        return student_service.authenticate(stud)

    def log_out(name: str) -> bool:
        # TODO: implementation required
        return( "Successfully Signed Out." )
        # exit(1)

if __name__ == "__main__":
    session_service = SessionService()
    print(session_service.log_in())
