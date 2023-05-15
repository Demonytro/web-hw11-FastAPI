from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactIsActiveModel


async def get_contacts(limit: int, offset: int, db: Session):
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_contact_by_nick(nick: str, db: Session):
    contact = db.query(Contact).filter_by(nick=nick).first()
    return contact


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())  # Owner(**body.dict())
    db.add(contact)
    db.commit()
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.nick = body.nick
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.description = body.description
        contact.is_active_contact = body.is_active_contact
        contact.user_id = body.user_id
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def set_is_active_contact(contact_id: int, body: ContactIsActiveModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.is_active_contact = body.is_active_contact
        db.commit()
    return contact
