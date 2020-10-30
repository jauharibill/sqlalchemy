from sqlalchemy import Table, Column, Integer, String, MetaData
from db import database

meta = MetaData()
conn = database()

users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('firstname', String),
              Column('lastname', String),
              Column('age', Integer),
              Column('phone', String))

meta.create_all(conn.engine)