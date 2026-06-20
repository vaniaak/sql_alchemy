from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///School.db')
engine.connect()

base = declarative_base()

class user(base):
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    personalid = Column(String)
    salary = Column(float)
    
base.metadata.creat_all(engine)

session = sessionmaker(bind=engine)
sessionlocal = session()

