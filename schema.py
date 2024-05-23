from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    loans: List["Loan"] = []

    class Config:
        orm_mode = True

class LoanBase(BaseModel):
    amount: float
    annual_interest_rate: float
    loan_term: int

class LoanCreate(LoanBase):
    owner_id: int

class Loan(LoanBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class LoanSchedule(BaseModel):
    month: int
    remaining_balance: float
    monthly_payment: float

class LoanSummary(BaseModel):
    current_principal_balance: float
    total_principal_paid: float
    total_interest_paid: float
