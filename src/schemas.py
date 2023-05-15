from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):

    first_name: str = Field('Dmytro', min_length=3, max_length=25)
    last_name: str = Field('Oseledko', min_length=3, max_length=25)
    email: EmailStr


class UserResponse(BaseModel):
    id: int = 1
    first_name: str = 'Dmytro'
    last_name: str = 'Oseledko'
    email: EmailStr

    class Config:
        orm_mode = True


class ContactModel(BaseModel):
    nick: str = Field('Badrunt', min_length=3, max_length=16)
    phone_number: str = Field('050-907-97-77')
    birthday: str = Field('10-04-2019')
    is_active_contact: Optional[bool] = True
    description: str
    user_id: int = Field(1, gt=0)


class ContactIsActiveModel(BaseModel):
    is_active_contact: bool = True


class ContactResponse(BaseModel):
    id: int = 1
    nick: str = 'Badrunt'
    phone_number: str = '050-907-97-77'
    birthday: str = '10-04-2019'
    email: EmailStr
    is_active_contact: bool = True
    description: str
    user: UserResponse

    class Config:
        orm_mode = True

# class OwnerModel(BaseModel):
#     email: EmailStr
#
#
# class OwnerResponse(BaseModel):
#     id: int = 1
#     email: EmailStr
#
#     class Config:
#         orm_mode = True
#
#
# class CatModel(BaseModel):
#     nick: str = Field('Barsik', min_length=3, max_length=16)
#     age: int = Field(1, ge=1, le=30)
#     vaccinated: Optional[bool] = False
#     description: str
#     owner_id: int = Field(1, gt=0)  # ge >=  gt >
#
#
# class CatVaccinatedModel(BaseModel):
#     vaccinated: bool = False
#
#
# class CatResponse(BaseModel):
#     id: int = 1
#     nick: str = 'Barsik'
#     age: int = 12
#     vaccinated: bool = False
#     description: str
#     owner: OwnerResponse
#
#     class Config:
#         orm_mode = True
