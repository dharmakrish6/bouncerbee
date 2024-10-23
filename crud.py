from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password,age=user.age,location=user.location)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def create_bouncer(db: Session, bouncer: schemas.BouncerCreate):
    db_bouncer = models.Bouncer(name=bouncer.name, phone_number=bouncer.phone_number, email=bouncer.email,age=bouncer.age,height=bouncer.height,weight=bouncer.weight,experience=bouncer.experience,city=bouncer.city)
    db.add(db_bouncer)
    db.commit()
    db.refresh(db_bouncer)
    return db_bouncer

def get_bouncer(db: Session, bouncer_id: int):
    return db.query(models.Bouncer).filter(models.Bouncer.id == bouncer_id).first()

def get_all_bouncers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Bouncer).offset(skip).limit(limit).all()

def get_bouncer_by_phone(db: Session, phone_number: str):
    return db.query(models.Bouncer).filter(models.Bouncer.phone_number == phone_number).first()
