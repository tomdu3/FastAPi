import uuid

from fastapi import FastAPI, status

from models import User

app = FastAPI()

users = {"1": {"name": "John", "age": 20}, "2": {"name": "Jane", "age": 21}}


@app.get("/users")
def users_list():
    return users


@app.get("/users/{user_id}")
def user_details(user_id: str):
    return users[user_id]
