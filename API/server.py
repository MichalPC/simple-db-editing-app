from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import pprint

#VERY UNSAFE#
client = MongoClient("mongodb+srv://michalpc:test1234@simple-user-login-app-d.ki5ky.mongodb.net/db?retryWrites=true&w=majority")
db = client['db']
collection = db['users']

app = FastAPI()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/exists/")
async def usernameEmpty():
    return {"err": "No username provided"}

@app.get("/exists/{username}")
async def userExists(username):
    userExists = collection.find({"username": username})
    if(userExists.count() == 1):
        return {"exists": True}
    return {"exists": False}

@app.get("/login/{username}/{password}")
async def userLogin(username, password):
    userExists = collection.find({"username": username})

    if(userExists.count() == 1):
        if(userExists[0]['password'] == password):
            return {"login": True}
    return {"login": False,
            "err": "Details provided were incorrect"}
