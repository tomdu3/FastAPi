from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from models import UserDB, User, Base
from database import engine, get_db

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency injection for the database session
@app.get("/users")
def users_list(db: Session = Depends(get_db)):
    users = db.query(UserDB).all()
    return users


@app.get("/users/{user_id}")
def user_details(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", status_code=status.HTTP_201_CREATED)
def user_add(user: User, db: Session = Depends(get_db)):
    db_user = UserDB(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "name": db_user.name, "age": db_user.age}


@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_update(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.name = user.name
    db_user.age = user.age
    db.commit()
    db.refresh(db_user)
    return "User updated"


@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_delete(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return "User deleted"



# import uuid

# from fastapi import FastAPI, status

# from models import User

# app = FastAPI()

# users = {"1": {"name": "John", "age": 20}, "2": {"name": "Jane", "age": 21}}


# @app.get("/users")
# def users_list():
#     return users


# @app.get("/users/{user_id}")
# def user_details(user_id: str):
#     return users[user_id]


# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def user_add(user: User):
#     users[str(uuid.uuid4())] = user
#     return "User added"


# @app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
# def user_update(user_id: str, user: User):
#     users[user_id] = user
#     return "User updated"


# @app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
# def user_delete(user_id: str):
#     del users[user_id]
#     return "User deleted"
