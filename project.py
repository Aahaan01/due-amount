def calculate_change(bill_amount, amount_paid):
    change = amount_paid - bill_amount
    return change

bill = 2.50
payment = 4.00

change_to_return = calculate_change(bill, payment)

print(f"The change you should get is: ${change_to_return:.2f}")
