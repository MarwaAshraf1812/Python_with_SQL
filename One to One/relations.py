from models1 import User, Profile
from sqlalchemy.orm import sessionmaker
from db import engine

session = sessionmaker()(bind=engine)

# Create a new user with profile
# user = User(name="John", email="john@example.com", password='12345678')
# session.add(user)
user = session.query(User).filter_by(id=1).first()
# profile = Profile(fname='John', lname='Smith', user=user)
# session.add(profile)
# session.commit()

# print(user.profile.fname)
# print(user.profile.lname)


#update
# user.profile.fname = 'Elon'
# user.profile.lname = 'Musk'
# session.commit()
#delete
session.delete(user)
session.commit()