from fastapi import FastAPI, Depends, HTTPException
import uvicorn
import Schema
import crud, models
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/students', response_model=Schema.Details)
async def get_details(Roll_no : int, db : Session = Depends(get_db)):
    db_student = crud.get_student(db, roll_no=Roll_no)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student details not found")
    return db_student

@app.post('/add-details/', response_model=Schema.Details)
async def add_details(details : Schema.Details, db : Session = Depends(get_db)):
    db_student = crud.get_student(db, roll_no=details.RollNo)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already registered")
    return crud.create_student(db, student=details)


# @app.post('/users/uploadfile')
# def upload_file(file: UploadFile = File(...)):
#     return {"Filename" : file.filename}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)