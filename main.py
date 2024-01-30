from fastapi import FastAPI
import uvicorn
from routes.route import router

app = FastAPI()
app.include_router(router)
#this is our homepage
@app.get('/')
async def homePage():
    return {"homepage"}
@app.get('/home')
async def home():
    return {"----homeURL----"}
if __name__ == "__main__":
    uvicorn.run(app=app,host='127.0.0.1',port=8000)