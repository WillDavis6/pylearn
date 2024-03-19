loan_amount = 415000
annual_interest_rate = 0.065
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = 2502
total_months = 30 * 12

value= 0

remaining_balance = loan_amount
print("Month\tInterest\tPrincipal\tBalance")
for month in range(1, total_months + 1):
    interest_payment = remaining_balance * monthly_interest_rates
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    print(f"{month}\t{interest_payment:.2f}\t\t{principal_payment:.2f}\t\t{remaining_balance:.2f}")

from flask_wtf import FlaskForm
class algorythm():
    print('')
