from sqlalchemy import Column, Integer, String
from database import base

class student(base):
    Rollno : Column(Integer, primary_key=True, index=True)
    Name : Column(String)
    Std : Column(String)
    EngMarks : Column(Integer)
    MathsMarks : Column(Integer)
    SciMarks : Column(Integer)
