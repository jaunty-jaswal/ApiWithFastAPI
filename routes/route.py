from fastapi import APIRouter,Body,Depends,HTTPException,status
from engine import readpdf,speech
from createpdf import create
# import json 
from schema.userSchema import (
    PostingSchema,
    SignupSchema,
    LoginSchema
)
from userauth.auth import encodeJwt
from userauth.verify import JwtHandler
from database.db import (
    add_user,
    add_content,
    read_content,
    collection2,
    dispText,
    textStore
)
import asyncio
from fastapi.encoders import jsonable_encoder
from kafka_client import producer,consumer
from consumer.consume import mainconsumer,caller
router = APIRouter()

async def checkuser(user:LoginSchema):
    async for i in collection2.find():
        if(user.email == i["email"] and user.password == i["password"]):
            return True
    return False
 
@router.get('/')
async def homePage():
    id = 0
    return {"HOMEPAGE"}

@router.get('/display')
async def poster():
    return await read_content()

@router.post('/post') #,dependencies=[Depends(JwtHandler())]
async def add_post(ourpost:PostingSchema):
    encoded = jsonable_encoder(ourpost)
    try :
        producer.send_one(encoded)
        #return {"Status":HTTPException(status_code=status.HTTP_201_CREATED)}
    except Exception as e:
        #return {"Response":HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,detail=str(e))}
        print(e)
    
    try :
        #consumer.Callconsumer().consumerhere()
        #await consumer.Callconsumer().data_adding()
        dats = {} 
        caller(dats) 
        # print(dats)
        await add_content(dats)
        return {"Response":"INSERTED"}
    except:
        return {"Response":HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)}

@router.post('/signup')
async def signup(ob:SignupSchema=Body(...)):
    obs = jsonable_encoder(ob) 
    await add_user(obs)
    return encodeJwt(ob.email)

@router.post('/login')
async def login(ob:LoginSchema=Body(...)):
    if await checkuser(ob):
        return encodeJwt(ob.email)
    return {
        "error":HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    }
@router.get('/userdetail')
async def userdetails():
    det = []
    mail = []
    async for i in collection2.find():
        det.append(i["name"])
        mail.append(i["email"])
    return {"usernames":det,"emails":mail}
@router.post('/text')
async def tesseracttext():
    txt = readpdf.return_text()
    id  = readpdf.returnid()
    index = len(id)-1
    if(index == 0 or index == -1):
        await textStore(txt,id[0])
    else :
        # print("+---------------------------------",index)
        await textStore(txt,id[index])
    return {"text:->",txt}
@router.get('/dbdata')
async def dBase():
    return {"Translation->":await dispText()
            }
@router.get('/createpdf')
async def createpdf():
    await create.createPDF()
# @router.get('/speech')
# async def speak():
#     await speech.textToSpeech()

@router.get('/speech')
async def speakUsingG():
    await speech.usingGoogle()
    

@router.get('/speech2')
async def speakUsingG2():
    await speech.usingGoogle2()