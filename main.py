from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)
    if not db_user or not crud.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful"}
##Bouncers APIs
@app.post("/register-bouncer", response_model=schemas.BouncerOut)

def register_bouncer(bouncer: schemas.BouncerCreate, db: Session = Depends(get_db)):
    db_bouncer = crud.get_bouncer_by_phone(db, phone_number=bouncer.phone_number)
    if db_bouncer:
        raise HTTPException(status_code=400, detail="Bouncer with this phone number already registered")
    return crud.create_bouncer(db=db, bouncer=bouncer)

@app.get("/bouncers/", response_model=list[schemas.BouncerOut])
def get_bouncers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bouncers = crud.get_all_bouncers(db, skip=skip, limit=limit)
    return bouncers
