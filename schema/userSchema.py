from pydantic import BaseModel,Field,EmailStr


class PostingSchema(BaseModel):
    title:str=Field(...)
    content:str=Field(...)


class SignupSchema(BaseModel):
    name:str=Field(...)
    email:EmailStr=Field(...)
    password:str=Field(...)


class LoginSchema(BaseModel):
    email:EmailStr=Field(...)
    password:str=Field(...)


class MailSchema(BaseModel):
    password:str=Field(...)
    mailid:str=Field(...)

