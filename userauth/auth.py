import jwt
import time
import os
from dotenv import load_dotenv
from database.pathsetter import setpath

conf = setpath.pathset().openyaml()
load_dotenv(conf["ENV"])
JWT_KEY = os.getenv("KEY")
JWT_ALGO = conf["ALGO"]
#encoding with jwt
def encodeJwt(email:str):
    data = {
        "email":email,
        "expiretime": time.time() + 1200 #(1200/60)= 20minutes
    }
    authorize_token = jwt.encode(data,key=JWT_KEY,algorithm=JWT_ALGO)
    return {"token-generated":authorize_token}

#decoding the generated token
#time.time() means the current time
def decodeJwt(token:str):
    decoded_token  = jwt.decode(token,key=JWT_KEY,algorithms=[JWT_ALGO])
    try: 
        if decoded_token['expiretime'] >= time.time():
            return decoded_token
        else:
            return None
    except:
        return {}




