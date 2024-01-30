from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from .auth import decodeJwt

class JwtHandler(HTTPBearer):
    def __init__(self,error:bool=True):
        super(JwtHandler,self).__init__(auto_error=error)

    async def __call__(self,request:Request):
        creds:HTTPAuthorizationCredentials = await super(JwtHandler,self).__call__(request)
        if creds:
            if not creds.scheme == 'Bearer':
                raise HTTPException(status_code=403,detail="invalid scheme")
            if not self.check(creds.credentials):
                raise HTTPException(status_code=403, detail="Token either invalid or expired")
            return creds.credentials
        else:
            raise HTTPException(status_code=403, detail="authorization code invalid")
 
    def check(self,token:str):
            istoken = False
            try:
                tokenright = decodeJwt(token)
            except:
                tokenright=None
            if tokenright:
                istoken=True
            else:
                istoken=False    
            return istoken
    

    



