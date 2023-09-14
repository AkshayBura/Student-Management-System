from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
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
        raise HTTPException(status_code=404, detail=f"Student with Roll No {Roll_no} doesn't exist")
    return db_student

@app.get('/allstudents')
async def all_students(db : Session = Depends(get_db)):
    db_student = db.query(models.student).all()
    return db_student

@app.post('/add-details')
async def add_details(details: Schema.Details = Depends(), db : Session = Depends(get_db)):
    db_student = crud.get_student(db, roll_no=details.RollNo)
    if db_student:
        raise HTTPException(status_code=400, detail="Student is already registered")
    return crud.create_student(db, student=details)

# @app.post('/add-details')
# async def add_details(details : Schema.Details = Depends(), db : Session = Depends(get_db), file : UploadFile = File(...)):
#     db_student = crud.get_student(db, roll_no=details.RollNo)
#     if db_student:
#         raise HTTPException(status_code=400, detail="Student is already registered")
#     crud.create_student(db, student=details)
#     file_path = f'D:/Training/Student Management System/{file.filename}'
#     with open(file_path,'wb') as obj:
#         obj.write(file.file.read())
#     return {"Info": f"File '{file.filename}' is saved at '{file_path}'", 'Details' : 'Student details added successfully'}

@app.put('/update-details/{Roll_No}', response_model=Schema.update_details)
async def update_details(Roll_No: int, details : Schema.update_details, db : Session = Depends(get_db)):
    db_student = crud.get_student(db, roll_no=Roll_No)
    if db_student:
        return crud.update_student(db, student=details, roll_no=Roll_No)
    raise HTTPException(status_code=404, detail=f"Student with Roll No {Roll_No} doesn't exist")

@app.delete('/delete-details/{Roll_No}')
async def delete_details(Roll_No : int, db : Session = Depends(get_db)):
    db_student = crud.get_student(db, roll_no=Roll_No)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student with Roll No {Roll_No} doesn't exist")
    return crud.delete_student(db, roll_no=Roll_No)

# @app.post('/users/uploadfile')
# def upload_file(file: UploadFile = File(...)):
#     return {"Filename" : file.filename}

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
