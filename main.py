from fastapi import FastAPI

app = FastAPI()

@app.get('/detail')
async def get_details(name : str):
    return {'Hello' : {name}}