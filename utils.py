import numpy as np

def calculate_amortization_schedule(amount, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = np.pmt(monthly_interest_rate, loan_term, -amount)
    schedule = []
    remaining_balance = amount

    for month in range(1, loan_term + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        schedule.append({
            "month": month,
            "remaining_balance": round(remaining_balance, 2),
            "monthly_payment": round(monthly_payment, 2)
        })

    return schedule

def calculate_loan_summary(schedule, month):
    total_principal_paid = sum(payment["monthly_payment"] - payment["remaining_balance"] * 0.05 for payment in schedule[:month])
    total_interest_paid = sum(payment["remaining_balance"] * 0.05 for payment in schedule[:month])
    current_principal_balance = schedule[month - 1]["remaining_balance"]
    
    return {
        "current_principal_balance": round(current_principal_balance, 2),
        "total_principal_paid": round(total_principal_paid, 2),
        "total_interest_paid": round(total_interest_paid, 2)
    }

