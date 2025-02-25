from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.user import users

user = APIRouter()

@user.get("/")
def read_root():
    return "inicio"


@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = {
        "id": data_user.id,
        "name": data_user.name,
        "username": data_user.username,
        "user_passw": data_user.user_passw
    }
    print(new_user["id"])
    print(new_user["name"])
    print(new_user["username"])
    print(new_user["user_passw"])
    insert_statement = users.insert().values(**new_user)
    print(insert_statement)
    conn.execute(insert_statement)
    return "Success"