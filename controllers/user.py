from models.user import User
from db import database
from sqlalchemy import select

class UserController:
    def __init__(self):
        self.conn = database()

    def index(self):
        row = self.conn.session.execute(select([User]))
        return row.fetchall()

    def create(self):
        return self.conn.session.add(User(
            firstname="Bill Tanthowi",
            lastname="Jauhari",
            age=26,
            phone="082245088948"))