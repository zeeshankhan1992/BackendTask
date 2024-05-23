# Loan Amortization API

This project is a REST API for a Loan Amortization app built using FastAPI, SQLAlchemy, and SQLite. The API allows clients to:

- Create a user
- Create a loan
- Fetch a loan schedule
- Fetch a loan summary for a specific month
- Fetch all loans for a user
- Share a loan with another user

## Features

- FastAPI for building APIs
- SQLAlchemy ORM for database interactions
- SQLite for the database
- Custom amortization schedule calculation

## Endpoints

- `POST /users/`: Create a new user
- `POST /loans/`: Create a new loan
- `GET /loans/{loan_id}/schedule/`: Fetch the amortization schedule for a loan
- `GET /loans/{loan_id}/summary/{month}`: Fetch the loan summary for a specific month
- `GET /users/{user_id}/loans/`: Fetch all loans for a user
- `POST /loans/{loan_id}/share/{user_id}/`: Share a loan with another user

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/loan-amortization-api.git
    cd loan-amortization-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create the SQLite database and tables:**

    The database and tables will be automatically created when you run the FastAPI application for the first time.

5. **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

6. **Open your browser and navigate to:**

    ```url
    http://127.0.0.1:8000/docs
    ```

    Here you will find the interactive API documentation provided by Swagger UI.

## File Structure
loan_amortization/
├── main.py # Entry point for the FastAPI app
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas for request and response models
├── database.py # Database connection and session management
├── crud.py # CRUD operations
├── utils.py # Utility functions, including the amortization schedule calculation
└── test_main.py # Tests for the API


## Testing

1. **Install testing dependencies:**

    ```bash
    pip install pytest
    ```

2. **Run the tests:**

    ```bash
    pytest
    ```

## Author

- zeeshankhan(https://github.com/zeeshankhan)


