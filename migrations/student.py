from sqlalchemy import Table, Column, Integer, String, MetaData
from db import database

meta = MetaData()
conn = database()

students = Table('students', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('lastname', String))

meta.create_all(conn.engine)