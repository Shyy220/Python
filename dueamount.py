bill_amount = float(input("Enter the total bill amount: "))

amount_paid = float(input("Enter the amount paid by the customer: "))

if amount_paid >= bill_amount:

    change = amount_paid - bill_amount
    print(f"Bill paid completely! Change to return: ${change:.2f}")
else:

    due_amount = bill_amount - amount_paid
    print(f"Remaining due amount to be paid: ${due_amount:.2f}")