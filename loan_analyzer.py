# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.
"""
loan_costs = [500, 600, 200, 1000, 450]


# Determines length of list loan_costs.

total_number_loans = len(loan_costs)

# Calculates sum of the list loan_costs.

sum_of_loans = sum(loan_costs)

# Determines the average price of the loans.

average_loan_price = sum_of_loans / total_number_loans

print(f"The total number of loans is: {total_number_loans}, The sum of all loan costs is: ${sum_of_loans}, The average cost of a loan is: ${average_loan_price}.")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

"""

# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Functions below get the value from the dictionary loan.

future_loan_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
#print(future_loan_value, remaining_months)

# The formula for Present Value is used to calculate a "fair value" of the loan.
# Minimum required return of 20% as the discount rate.

annual_discount_rate = 0.2
# Function created to calculate present value.
def current_loan_value(future_value,remaining_months):
    present_value = future_value / (1 + (annual_discount_rate)/12) ** remaining_months
    return present_value

# Function called.
present_loan_value = current_loan_value(future_loan_value, remaining_months)
# Loan value printed.
print(f"The Present Value of the lone is: ${present_loan_value: .2f}")

# If statement is used to determine if present loan value is worth it based on the current loan price.
if present_loan_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#*********Note*****************************Function was defined above in line 51********************************************************

#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

# Function from line 51 (current_loan_value) called.
present_value = current_loan_value (new_loan.get("future_value"), new_loan.get("remaining_months"))

# Value of new loan printed.
print(f"The present value of the loan is: ${present_value: .2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Created an empty list called `inexpensive_loans`

inexpensive_loans = []

#Looped through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)


# Printed the `inexpensive_loans` list

print(inexpensive_loans)

"""Part 5: Save the results.
"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use of csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

    