from fastapi.testclient import TestClient
from .main import app
from .database import SessionLocal, engine
from .models import Base
from .schemas import UserCreate, LoanCreate

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_create_loan():
    response = client.post("/loans/", json={"amount": 10000, "annual_interest_rate": 5, "loan_term": 24, "owner_id": 1})
    assert response.status_code == 200
    assert response.json()["amount"] == 10000

def test_get_loan_schedule():
    response = client.get("/loans/1/schedule/")
    assert response.status_code == 200
    assert len(response.json()) == 24

def test_get_loan_summary():
    response = client.get("/loans/1/summary/12")
    assert response.status_code == 200
    assert "current_principal_balance" in response.json()
