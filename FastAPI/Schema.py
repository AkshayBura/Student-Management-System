from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

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

class update_details(BaseModel):

    Email : Optional[str] = None
    Name : Optional[str] = None
    EngMarks : Optional[int] = None
    MathsMarks : Optional[int] = None
    SciMarks : Optional[int] = None
  
    class Config:
        orm_mode = True