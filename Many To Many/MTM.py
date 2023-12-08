from model3 import User, Group, group_user
from sqlalchemy.orm import sessionmaker
from database import engine

session = sessionmaker()(bind=engine)

# session.add_all(
#     [
#         User(username="John"),
#         User(username="Jane"),
#         User(username="Jack"),
#         User(username="Janet"),
#     ])
# session.commit()


# session.add_all(
#     [
#         Group(gname="JS"),
#         Group(gname="PHP"),
#         Group(gname="Python"),
#         Group(gname="C"),
#     ])
# session.commit()

u1 = session.query(User).filter_by(id=1).first()
u2 = session.query(User).filter_by(id=2).first()
u3 = session.query(User).filter_by(id=3).first()
u4 = session.query(User).filter_by(id=4).first()

g1 = session.query(Group).filter(Group.id==1).first()
g2 = session.query(Group).filter(Group.id==2).first()
g3 = session.query(Group).filter(Group.id==3).first()
g4 = session.query(Group).filter(Group.id==4).first()

# u1.groups.append(g1)
# u1.groups.append(g2)
# u1.groups.append(g3)
# u1.groups.append(g4)
# session.commit()

# u2.groups.append(g1)
# u2.groups.append(g2)
# u2.groups.append(g3)
# session.commit()


# u3.groups.append(g1)
# u3.groups.append(g2)
# session.commit()

# u4.groups.append(g2)
# u4.groups.append(g4)
# session.commit()

# print(u1.groups)
# print(u2.groups)
# print(u3.groups)
# print(u4.groups)
# print(g1.users)
# print(g2.users)
# print(g3.users)
# print(g4.users)


#ana ghyart username from groupowner
# g1.users[0].username = "Elon"
# session.commit()

#ana ghyart gname from userowner
# u1.groups[0].gname = "JAVA"
# session.commit()

# u1.groups.remove(g2)
# session.commit()

g1.users.remove(u2)
session.commit()