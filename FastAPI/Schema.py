from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Details(BaseModel):

    RollNo : int
    Email : str
    Name : str
    EngMarks : int
    MathsMarks : int
    SciMarks : int
    class Config:
        orm_mode = True
