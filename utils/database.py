from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb+srv://codesprinters:2Df681Ol3qyaBZFO@cluster0.hux4geu.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGODB_URL)

db = client['ecommerce']


