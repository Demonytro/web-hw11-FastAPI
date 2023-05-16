from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_users(db: Session):
    users = db.query(User).all()
    return users


async def get_users_birthday(birthday: str, db: Session):
    users = db.query(User).filter_by(birthday=birthday).all()
    return users


async def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter_by(id=user_id).first()
    return user


async def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter_by(email=email).first()
    return user


async def get_users_by_first_name(first_name: str, db: Session):
    users = db.query(User).filter_by(first_name=first_name).all()
    return users


async def get_users_by_last_name(last_name: str, db: Session):
    users = db.query(User).filter_by(last_name=last_name).all()
    return users


async def create(body: UserModel, db: Session):
    user = User(**body.dict())  # Owner(**body.dict())   User(email=body.email)
    db.add(user)
    db.commit()
    return user


async def update(user_id: int, body: UserModel, db: Session):
    user = await get_user_by_id(user_id, db)
    if user:
        user.email = body.email
        db.commit()
    return user


async def remove(user_id: int, db: Session):
    user = await get_user_by_id(user_id, db)
    if user:
        db.delete(user)
        db.commit()
    return user
