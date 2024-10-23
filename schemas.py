from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    age:str
    location:str

class UserInDB(UserCreate):
    hashed_password: str

class UserOut(BaseModel):
    username: str

    class Config:
        orm_mode = True


class BouncerCreate(BaseModel):
    name: str
    phone_number: str
    email: str
    age:str
    height:str
    weight:str
    experience:str
    city:str

class BouncerOut(BaseModel):
    id: int
    name: str
    phone_number: str
    email: str
    age:str
    height:str
    weight:str
    experience:str
    city:str

    class Config:
        orm_mode = True