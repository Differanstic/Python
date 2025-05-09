'''

@ Discount Condition
    1. If the amount is greater than 5000, apply a discount of 5%.
    
    or 
    
    2. Membership discount of 5% if the user is a member.

'''

# Discount 5% on Shopping
discount_rate = 5


amount = float(input("Enter the amount of your purchase: "))
isMember = input("Are you a member? (yes/no): ").strip().lower()

if amount >= 5000 or isMember == "yes":
    # Discount Amount
    discount_amount = amount * discount_rate / 100 
    amount = amount - discount_amount
    print("Discount amount: ", discount_amount)

    

print("Amount to be paid : ", amount)
