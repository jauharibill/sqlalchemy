from controllers.user import UserController
from controllers.student import StudentController

user = UserController()
student = StudentController()

user_data = ["dian romadlonal", "adzim"]

if __name__ == "__main__":
    user.update(2, user_data)
