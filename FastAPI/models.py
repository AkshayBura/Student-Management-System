from sqlalchemy import Column, Integer, String
from database import Base

class student(Base):
    __tablename__ = "student"

    RollNo = Column(Integer, primary_key=True, index=True)
    Email = Column(String, unique=True, index=True)
    Name = Column(String)
    EngMarks = Column(Integer)
    MathsMarks = Column(Integer)
    SciMarks = Column(Integer)
