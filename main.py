from fastapi import FastAPI
import uvicorn
from routes.route import router

app = FastAPI()
app.include_router(router)
@app.get('/')
async def homePage():
    return {"homepage"}
if __name__ == "__main__":
    uvicorn.run(app=app,host='127.0.0.1',port=8000)