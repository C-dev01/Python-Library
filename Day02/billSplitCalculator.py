# WAP that takes total bill amount and number of friends as input and 
# Calculate how much each person will pay.
# Also print the datatype of each variable used
# (Hint : Use float() and division operator)

bill = float(input("Enter total bill amount : "))
friends = int(input("Number of Friends : "))

amountToPay = bill/friends

print("Each will pay : ",round(amountToPay,2))