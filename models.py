from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    loans = relationship("Loan", back_populates="owner")

class Loan(Base):
    __tablename__ = "loans"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    annual_interest_rate = Column(Float)
    loan_term = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="loans")
    shared_with = relationship("User", secondary="loan_shares")

class LoanShare(Base):
    __tablename__ = "loan_shares"
    
    loan_id = Column(Integer, ForeignKey("loans.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
