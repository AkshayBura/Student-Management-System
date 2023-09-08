from sqlalchemy.orm import Session

import models, Schema


def get_student(db: Session, roll_no: int):
    return db.query(models.student).filter(models.student.RollNo == roll_no).first()

def delete_student(db: Session, roll_no: int):
    db.query(models.student).filter(models.student.RollNo == roll_no).delete(synchronize_session=False)
    db.commit()
    return f'Successfully deleted student with Roll No {roll_no}'

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

def update_student(db: Session,roll_no: int, student: Schema.update_details):
    db_student = db.query(models.student).filter(models.student.RollNo == roll_no)
    db_student = db_student.update(student.__dict__)
    db.commit()
    # db.refresh(db_student)
    return student