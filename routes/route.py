from fastapi import APIRouter,Body,Depends
from schema.userSchema import (
    PostingSchema,
    SignupSchema,
    LoginSchema
)
from userauth.auth import encodeJwt
from userauth.verify import JwtHandler
from database.db import (
    add_content,
    add_user,
    read_content,
    collection2
)
from fastapi.encoders import jsonable_encoder
router = APIRouter()

async def checkuser(user:LoginSchema):
    async for i in collection2.find():
        if(user.email == i["email"] and user.password == i["password"]):
            
            return True
    return False

            
@router.get('/display')
async def poster():
    return await read_content()


@router.post('/post',dependencies=[Depends(JwtHandler())])
async def add_post(ourpost:PostingSchema):
    encoded = jsonable_encoder(ourpost)
    await add_content(encoded)
    return {"OK","Post Added"}

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
        "error":"wrong details"
    }
@router.get('/userdetail')
async def userdetails():
    det = []
    mail = []
    async for i in collection2.find():
        det.append(i["name"])
        mail.append(i["email"])
    return {"usernames":det,"emails":mail}


