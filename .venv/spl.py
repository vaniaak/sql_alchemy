from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///Students.db')
engine.connect()

base = declarative_base()

class user(base):
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    Score = Column(Integer)
    
base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionlocal = session()

user1 = user(name = 'sam', Score = 20)
user2 = user( name = 'saeed', Score = 18)

sessionlocal.add_all([user1, user2])
sessionlocal.commit()

user_lists = sessionlocal.query(user).all()
print(user_lists)

for user in user_lists:
    print(user.name)
    print(user.Score)
    
user_by_id = sessionlocal.query(user).filter_by(id=2).first()
print(user_by_id.filed, user_by_id.name)

temp2 = sessionlocal.query(user).filter(user.name.like("%S%")).all()
print(temp2[0].name)

user_update = sessionlocal.query(user).filter_by(id=1).first()
if user_update:
    user_update.name = "Reza"
    user_update.score = 20
    sessionlocal.commit()
    
user = sessionlocal.qery(user).filter_by(id=1).first()
if user != None:
    sessionlocal.delete(user)
    sessionlocal.commit()
else:
    print('your id dose not exist')
    
user = sessionlocal.query(user).filter_by(name = 'nima').first()
user.name = 'ahmad'
user.Score = 17
sessionlocal.commit()