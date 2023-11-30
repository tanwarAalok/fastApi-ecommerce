from fastapi import FastAPI
from routes.userRouters import userRouter
app = FastAPI()




app.include_router(userRouter, prefix="/api/v1/users")
