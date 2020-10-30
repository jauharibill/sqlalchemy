from models.user import User
from db import database
from sqlalchemy import select

class UserController:
    def __init__(self):
        self.conn = database()

    def index(self):
        return self.conn.\
            session.\
            execute(select([User])).\
            fetchall()

    def create(self, data):

        firstname = data[0]
        lastname = data[1]
        age = data[2]
        phone = data[3]

        self.conn.session.add(User(
            firstname=firstname,
            lastname=lastname,
            age=age,
            phone=phone))

        return self.conn.session.commit()

    def show(self, id):
        return self.conn.session.query(User).filter(User.id==id)

    def update(self, id, data):
        user = self.conn.session.query(User).get(id)
        user.firstname = data[0]
        user.lastname = data[1]
        return self.conn.session.commit()