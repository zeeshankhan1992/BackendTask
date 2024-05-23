from sqlalchemy.orm import Session
from . import models, schemas, utils

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_loan(db: Session, loan: schemas.LoanCreate):
    db_loan = models.Loan(amount=loan.amount, annual_interest_rate=loan.annual_interest_rate, loan_term=loan.loan_term, owner_id=loan.owner_id)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def get_loan_schedule(db: Session, loan_id: int):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return utils.calculate_amortization_schedule(loan.amount, loan.annual_interest_rate, loan.loan_term)

def get_loan_summary(db: Session, loan_id: int, month: int):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    schedule = utils.calculate_amortization_schedule(loan.amount, loan.annual_interest_rate, loan.loan_term)
    if month < 1 or month > loan.loan_term:
        raise HTTPException(status_code=400, detail="Invalid month")
    return utils.calculate_loan_summary(schedule, month)

def get_loans_for_user(db: Session, user_id: int):
    return db.query(models.Loan).filter(models.Loan.owner_id == user_id).all()

def share_loan(db: Session, loan_id: int, user_id: int):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if loan is None or user is None:
        raise HTTPException(status_code=404, detail="Loan or User not found")
    db_loan_share = models.LoanShare(loan_id=loan_id, user_id=user_id)
    db.add(db_loan_share)
    db.commit()
    return loan
