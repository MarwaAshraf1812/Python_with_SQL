from db import Base, engine
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'userss'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)  # Allow NULL values

    def __repr__(self) -> str:
        return f'User(name={self.name}, email={self.email})'

Base.metadata.create_all(bind=engine)