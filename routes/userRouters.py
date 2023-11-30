
from bson import ObjectId
from fastapi import APIRouter
from models.user_model import User
from utils.database import db

userRouter = APIRouter()
collection = db['users']


@userRouter.post("/")
async def create_user(body: User):
    body_dict = dict(body)
    res = await collection.insert_one(body_dict)
    body_dict["_id"] = str(res.inserted_id)
    return body_dict


@userRouter.get("/")
async def get_users():
    users = await collection.find().to_list(None)
    for user in users:
        user["id"] = str(user.pop("_id"))
    return users


@userRouter.put("/{user_id}")
async def update_user(user_id: str, body: User):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    for key in user:
        if key is not None:
            user[key] = body[key]

    await collection.update_one({"_id": ObjectId(user_id)}, {"$set": dict(body)})

    return {"message": "User updated successfully"}


@userRouter.delete("/{user_id}")
async def delete_user(user_id: str):
    await collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted successfully"}
