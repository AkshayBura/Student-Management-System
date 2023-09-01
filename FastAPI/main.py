from fastapi import FastAPI
from . import Schema


app = FastAPI()

@app.get('/')
async def hello(name : str):
    return {'Hello':{name}}

@app.post('/add-details')
async def add_details(details : Schema.Details):
    return details