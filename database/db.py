from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import bson
import os
from dotenv import load_dotenv
from database.pathsetter import setpath
from fastapi import HTTPException,status

from fastapi.encoders import jsonable_encoder
conf = setpath.pathset().openyaml()
load_dotenv(conf["ENV"]["MONGOENV"])
MONGO_SERVER =os.getenv("MONGO_ID")


client = AsyncIOMotorClient(MONGO_SERVER)
database = client.jwtData
collection1 = database.get_collection(conf["COLLECTIONS"]['DATACOLLECTION'])
collection2 = database.get_collection(conf["COLLECTIONS"]['USERCREDENTIALSCOLLECTION'])
collection3 = database.get_collection(conf["COLLECTIONS"]["TEXTDATACOLL"])

def textSchema(text):
    return {"Translation":text}

def parser(content):
    return {
        "title": content["title"],
        "content": content['content']
    }
def userparser(user):
    return {
        "name":user["name"],
        "email":user["email"],
        "password":str(user["password"])
    }

async def add_content(content):
    print("---content before---")
    await collection1.insert_one(content)
    print("---content after---")
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

async def textStore(text,id):
    text = jsonable_encoder(text)
    t = dict()
    t[f"data{id}"] = text
    await collection3.insert_one(t)
    
async def dispText():
    dats = []
    async for document in collection3.find():
    # Convert ObjectId to string
     ourdoc = {}
     for key, value in document.items():
        if(key != "_id"):
            if isinstance(value, bson.ObjectId):
                ourdoc[key] = str(value)
            else:
                ourdoc[key] = value
            dats.append("______________________")
            dats.append(ourdoc[key])
    return dats
