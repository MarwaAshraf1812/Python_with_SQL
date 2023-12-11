from socialMedia import User, Post, Like, addPost, addUser, addLike
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
# User_id = "e858b302-b4ab-49f3-b1e8-ce86c32f9628"
# PostContent = "The second post from the same user"
# new_post = Post(User_id, PostContent)
# session.add(new_post)
# session.commit()

# Create a user
# FirstName = "John"
# LastName = "Matrix"
# Email = "Jonny98@examplecom"
# ProfileName = "John6789" 
# addUser(FirstName, LastName, ProfileName, Email, session)

#Create a user
# FirstName = "Maya"
# LastName = "Musk"
# Email = "Yoyo98@example.com"
# ProfileName = "Yoyo6789"
# addUser(FirstName, LastName, ProfileName, Email, session)

#check dublicated users with filter(email)
# FirstName = "Emly"
# LastName = "Johnson"
# Email = "Emy98@example.com"
# ProfileName = "Emy6789"
# addUser(FirstName, LastName, ProfileName, Email, session)

#Create a post
# User_id = "e858b302-b4ab-49f3-b1e8-ce86c32f9628"
# PostContent = "The second post from the same user"
# addPost(User_id, PostContent, session)

#Create a post
# User_id = "d7783248-69a9-4a16-a59e-e6460c7321dd"
# PostContent = "The first post from the second user"
# addPost(User_id, PostContent, session)

# User_id = "d7783248-69a9-4a16-a59e-e6460c7321dd"
# PostContent = "The second post from the second user"
# addPost(User_id, PostContent, session)

#Create a post
# User_id = "ecdc4152-1a3f-44f0-87b7-2638a5bcdb80"
# PostContent = "The first post from third user"
# addPost(User_id, PostContent, session)

#Create a post
User_id = "ecdc4152-1a3f-44f0-87b7-2638a5bcdb80"
# PostContent = "The second post from third user"
# addPost(User_id, PostContent, session)

# allPosts = session.query(Post).filter(Post.User_id == User_id).all()

# postsFilterByUser = [p.PostContent for p in allPosts]
# print(postsFilterByUser)

#add like
# User_id = "ecdc4152-1a3f-44f0-87b7-2638a5bcdb80"
# Post_id = "83d017b8-137f-493a-b99b-a0a991b57dae"
# addLike(User_id, Post_id, session)

# User_id = "ecdc4152-1a3f-44f0-87b7-2638a5bcdb80"
# Post_id = "88c592fd-9e1b-4ac5-95de-82efd26935c4"
# addLike(User_id, Post_id, session)

# User_id = "d7783248-69a9-4a16-a59e-e6460c7321dd"
# Post_id = "88c592fd-9e1b-4ac5-95de-82efd26935c4"
# addLike(User_id, Post_id, session)

User_id = "6e63a2df-32bf-4304-8143-a905b0fd20d5"
Post_id = "88c592fd-9e1b-4ac5-95de-82efd26935c4"
# addLike(User_id, Post_id, session)

postLikes = session.query(Like).filter(Like.PostId==Post_id).all()
print(len(postLikes))

#Join
usersWhoLikedPost = session.query(User, Like).filter(Like.PostId == Post_id).filter(Like.UserId == User_id).all()
for u in usersWhoLikedPost:
    print(u["users"].FirstName, u["users"].LastName)