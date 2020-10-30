from controllers.user import UserController
from controllers.student import StudentController

user = UserController()
student = StudentController()

if __name__ == "__main__":
    user.index()
    student.index()
