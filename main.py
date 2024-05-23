from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/loans/", response_model=schemas.Loan)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return crud.create_loan(db=db, loan=loan)

@app.get("/loans/{loan_id}/schedule/", response_model=List[schemas.LoanSchedule])
def get_loan_schedule(loan_id: int, db: Session = Depends(get_db)):
    return crud.get_loan_schedule(db=db, loan_id=loan_id)

@app.get("/loans/{loan_id}/summary/{month}", response_model=schemas.LoanSummary)
def get_loan_summary(loan_id: int, month: int, db: Session = Depends(get_db)):
    return crud.get_loan_summary(db=db, loan_id=loan_id, month=month)

@app.get("/users/{user_id}/loans/", response_model=List[schemas.Loan])
def get_loans_for_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_loans_for_user(db=db, user_id=user_id)

@app.post("/loans/{loan_id}/share/{user_id}/", response_model=schemas.Loan)
def share_loan(loan_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud.share_loan(db=db, loan_id=loan_id, user_id=user_id)
