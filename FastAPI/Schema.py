from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Details(BaseModel):
    RollNo : int
    Name : str
    Std : str
    EngMarks : int
    MathsMarks : int
    SciMarks : int
