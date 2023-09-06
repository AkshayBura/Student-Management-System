from sqlalchemy.orm import Session

import models, Schema


def get_student(db: Session, roll_no: int):
    return db.query(models.student).filter(models.student.RollNo == roll_no).first()

# def get_student_by_email(db: Session, email: str):
#     return db.query(models.student).all()

# def get_students(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.student).offset(skip).limit(limit).all()


def create_student(db: Session, student: Schema.Details):
    db_student = models.student(RollNo = student.RollNo, Email = student.Email, Name = student.Name, EngMarks = student.EngMarks, MathsMarks = student.MathsMarks, SciMarks = student.SciMarks)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student