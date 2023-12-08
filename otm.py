from model2 import User, Post
from sqlalchemy.orm import sessionmaker
from dataBase import engine

session = sessionmaker()(bind=engine)

# user = User(username="maryam", password='12345678', email='maryam@example.com')
# session.add(user)
# session.commit()

posts = [
    {
        "post" : "learn sqlalchemy"
    },
    {
        "post" : "learn Python"
    },
    {
        "post" : "learn Django"
    }
]
user = session.query(User).filter_by(id=1).first()
# for p in posts:
#     new_post = Post(
#         post=p["post"],
#         user = user
#     )
#     session.add(new_post)
#     session.commit()

p1 = session.query(Post).filter(Post.id == 1).first()
# print(p1.user.id)
# print(p1.user.username)
# print(p1)

# p2 = Post(post="learn API")
# user.posts.append(p2)
# session.commit()


# p1.post = "update from post object"
# session.commit()

# user.posts[2].post = "update from user object"
# session.commit()

session.delete(user)
session.commit()