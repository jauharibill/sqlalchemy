from db import database
from sqlalchemy import select
from models.student import Student

class StudentController:
    def __init__(self):
        self.conn = database()

    def index(self):
        return self.conn.\
            session.\
            execute(select([Student])).\
            fetchall()