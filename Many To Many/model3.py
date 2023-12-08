from database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

#association table
group_user = Table(
    "group_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True)
)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    groups = relationship("Group", secondary=group_user, back_populates="users")

    def __repr__(self) -> str:
        return f"User: {self.username}"

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    gname = Column(String(50), nullable=False)
    users = relationship("User", secondary=group_user, back_populates="groups")

    def __repr__(self) -> str:
        return f"Group: {self.gname}"



Base.metadata.create_all(bind=engine)