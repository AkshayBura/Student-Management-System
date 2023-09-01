from fastapi import FastAPI

app = FastAPI()

@app.get('/detail')
async def hello(name : str):
    return {'Hello':{name}}

@app.get('/student/{id}')
async def get_detail(id = int):
    return {{id} : "Akshay"}