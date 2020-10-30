from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class database:
    def __init__(self):
        engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/aggregator-migration")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.engine = engine

