from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas import UserResponse, UserModel
from src.repository import users as repository_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = await repository_users.get_users(db)
    return users


# ----------begin------------------------------------------------------------------------------------
@router.get("/", response_model=List[UserResponse])
async def get_users_by_first_name(first_name: str, db: Session = Depends(get_db)):
    users = await repository_users.get_users_by_first_name(first_name, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return users


@router.get("/", response_model=List[UserResponse])
async def get_users_by_last_name(last_name: str, db: Session = Depends(get_db)):
    users = await repository_users.get_users_by_last_name(last_name, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return users


@router.get("/", response_model=UserResponse)
async def get_user_by_email(body: UserModel, db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return user
# -----------end-------------------------------------------------------------------------------------


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED) # ???????????????? 201 or 409
async def create_user(body: UserModel, db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.email, db) # ????????????????????????
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is exists!")  # ????????????
    user = await repository_users.create(body, db)
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(body: UserModel, user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.update(user_id, body, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return user


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.remove(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return user
