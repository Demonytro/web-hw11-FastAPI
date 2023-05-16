from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True)
    birthday = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


# class Contact(Base):
#     __tablename__ = "contacts"
#     id = Column(Integer, primary_key=True, index=True)
#
#     nick = Column(String, unique=True, index=True)
#     phone_number = Column(String, unique=True)
#     birthday = Column(String)
#     is_active_contact = Column(Boolean, default=True)
#     description = Column(String)
#
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
#     user = relationship("User", backref="contacts")
#
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())





# class Owner(Base):
#     __tablename__ = "owners"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
#
#
# class Cat(Base):
#     __tablename__ = "cats"
#
#     id = Column(Integer, primary_key=True, index=True)
#     nick = Column(String, index=True)
#     age = Column(Integer)
#     vaccinated = Column(Boolean, default=False)
#     description = Column(String)
#     owner_id = Column(Integer, ForeignKey("owners.id"), nullable=True)
#     owner = relationship("Owner", backref="cats")
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())