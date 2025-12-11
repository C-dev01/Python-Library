# Expense Tracker

expenses = [] # list of all expenses in form of dictionary
print("Welcome to Expense Tracker 💸")

while True: 
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit") 

    choice = int(input("Please Enter Your Choice : "))

# Add Expense
    if(choice == 1):
        date = input("Enter date (DD-MM-YYYY):")
        category = input("Enter category (Food, Travel, Shopping, etc):")
        description = input("Enter short description:")
        amount = int(input("Enter amount (₹):"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenses.append(expense)
        print("\nExpense Added!")

# View All Expenses
    elif(choice == 2):
        if (len(expenses) == 0):
            print("No Expenses Added!")
        else:
            print("====Your Expenses====")
            count = 1
            for eachItem in expenses:
                print(f"Expense{count}-> {eachItem["date"]}, {eachItem["category"]}, {eachItem["description"]}, {eachItem["amount"]}")
                count = count + 1

                
# View All Expense

    elif(choice == 3):
        total = 0
        for eachItem in expenses:
            total = total + eachItem["amount"]
        print("TOTAL EXPENSE : ",total)    

# Exit
    elif(choice == 4):
        print("Thanks for using our system 🙏🏻")
        break

    else:
        print("INVALID CHOICE! Try Again!")
