from db import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False )
    password = Column(String(30), nullable=False) 
    profile = relationship('Profile', backref='user', uselist=False, cascade="all, delete, delete-orphan")
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.email}, {self.password}"

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    fname = Column(String(50))
    lname = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f"{self.fname}, {self.lname}"


Base.metadata.create_all(bind=engine)