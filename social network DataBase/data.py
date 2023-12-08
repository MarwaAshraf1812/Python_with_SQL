from socialMedia import User, Post
from sqlalchemy.orm import sessionmaker
from dataBase import engine

session = sessionmaker()(bind=engine)
# Create a user
# FirstName = "Edward"
# LastName = "Clark"
# Email = "Eddy@example.com"
# ProfileName = "Eddy123"

# session.add_all(
#     [User(FirstName=FirstName, 
#         LastName=LastName, 
#         Email=Email, 
#         ProfileName=ProfileName
#     )])
# session.commit()

# Create a post
User_id = "e858b302-b4ab-49f3-b1e8-ce86c32f9628"
PostContent = "The second post from the same user"
new_post = Post(User_id, PostContent)
session.add(new_post)
session.commit()