from student_service import Student_Service

class SessionService: 

    def __init__(self) -> None:
        pass

    def log_in(name: str) -> bool:
        student_service = Student_Service()
        student_service.authenticate()

    def log_out(name: str) -> bool:
        # TODO: implementation required
        print( "Successfully Signed Out." )
        exit(1)

if __name__ == "__main__":
    session_service = SessionService()
    print(session_service.log_in())
