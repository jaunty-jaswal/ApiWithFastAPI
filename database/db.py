from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from database.pathsetter import setpath
from fastapi import HTTPException,status

conf = setpath.pathset().openyaml()
load_dotenv(conf["ENV"]["MONGOENV"])
MONGO_SERVER =os.getenv("MONGO_ID")


client = AsyncIOMotorClient(MONGO_SERVER)
database = client.jwtData
collection1 = database.get_collection(conf["COLLECTIONS"]['DATACOLLECTION'])
collection2 = database.get_collection(conf["COLLECTIONS"]['USERCREDENTIALSCOLLECTION'])


def parser(content):
    return {
        "title":str(content["title"]),
        "content": content['content']
    }
def userparser(user):
    return {
        "name":user["name"],
        "email":user["email"],
        "password":str(user["password"])
    }

async def add_content(content):
    await collection1.insert_one(content)
    return {"status":HTTPException(status_code=status.HTTP_200_OK)}

async def add_user(user):
    await collection2.insert_one(user)
    return {"status":HTTPException(status_code=status.HTTP_200_OK)}

async def read_content():
    array=[]
    async for i in collection1.find():
        array.append(parser(i))
    return array

async def read_user():
    user  = []
    async for i in collection2.find():
        user.append(userparser(i))
    return user
