from dataBase import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return uuid.uuid4()
class User(Base):
    __tablename__ = "users"
    #uuid4 return object not inter
    User_id = Column("UserID", String(36), primary_key=True,  default=lambda: str(uuid.uuid4()))
    FirstName = Column("FirstName", String(50), nullable=False)
    LastName = Column("LastName", String(50), nullable=False)
    Email = Column("Email", String(50), nullable=False)
    ProfileName = Column("ProfileName", String(50), nullable=False)

    def __repr__(self):
        return f"User(User_id={self.User_id}, FirstName={self.FirstName}, LastName={self.LastName}, Email={self.Email}, ProfileName={self.ProfileName})"

    def __init__(self, FirstName, LastName, ProfileName, Email):
        self.FirstName = FirstName
        self.LastName = LastName
        self.ProfileName = ProfileName
        self.Email = Email

class Post(Base):
    __tablename__ = "posts"
    Post_id = Column("PostID", String(36), primary_key=True,  default=lambda: str(uuid.uuid4()))
    User_id = Column("UserID", String(36), ForeignKey("users.UserID"), nullable=False)
    PostContent = Column("PostContent", String(50), nullable=False)

    def __repr__(self):
        return f"Post(Post_id={self.Post_id}, User_id={self.User_id}, Post={self.Post})"

    def __init__(self, User_id, PostContent):
        self.User_id = User_id
        self.PostContent = PostContent
Base.metadata.create_all(bind=engine)