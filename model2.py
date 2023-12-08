from dataBase import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "userst"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    posts = relationship("Post", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self) -> str:
        return f"{self.username}, {self.email}, {self.password}"

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    post = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('userst.id'))
    user = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"{self.post}"

Base.metadata.create_all(bind=engine)