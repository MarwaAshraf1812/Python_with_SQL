from models import User
from sqlalchemy.orm import sessionmaker
from db import engine

session = sessionmaker()(bind=engine)
# user1 = User(name='zeyad', email='zeyad@example.com')
# user2 = User(name='muhamed', email='zeyad@example.com')
# user3 = User(name='soso', email='zeyad@example.com')
# user4 = User(name='yara', email='zeyad@example.com')
# session.add_all([user1, user2, user3, user4])

# users = [
#     User(name='zeyad', email='zeyad@example.com'),
#     User(name='muhamed', email='muhammed@example.com'),
#     User(name='soso', email='soso@example.com'),
#     User(name='yara', email='yara@example.com'),
# ]
# # 
# for user in users:
#     session.add(user)
#     session.commit()

# users = session.query(User).all()
# for user in users:
#     print(user.name)
#     print(user.email)
#     print('------------------')

# user = session.query(User).filter(User.id == 3).first()
# print(user)

# update_user = session.query(User).filter(User.id == 1).first()
# print(update_user.name)
# update_user.name = 'marwa'
# session.commit()
# print(update_user.name)

# delete_user = session.query(User).filter(User.id == 1).first()
# session.delete(delete_user)
# session.commit()

#momken ast5dmha m3 filter and without filter
# user = session.query(User).first()
# print(user)

#hatrmy expeption -- with filter -- wlw fe ay error hay2ol
#user = session.query(User).one()
# user = session.query(User).filter(User.id == 8).one()
# print(user)

#lw al condition false hatrmy none
# user = session.query(User).filter(User.id == 20).scalar()
# print(user)

# users = session.query(User).all()
#last user 
# print(users[::-1][0])

# users = session.query(User).filter(User.name.startswith('m')).all()
# print(users)

# user = session.query(User).filter(User.id == 2, User.name == 'zeyad').all()

# user = session.query(User).order_by(User.id.desc()).first()
# print(user)

# filter > *args -- filter by > **kwargs
# users = session.query(User).filter_by(name='zeyad').all()
# print(users)
