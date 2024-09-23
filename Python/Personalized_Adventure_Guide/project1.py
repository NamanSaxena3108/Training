name=input("Hello User 😊 Please Enter Your Name \n")

print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")
try:
    destination=input("Where do you want to go").strip().lower()
    if destination == "mountain":
        print("You are going to the mountain")
    elif destination == "beach":
        print("You are going to the beach")
    else:
        print("Enter the correct choice")
    
    budget=int(input("Enter the budget : "))
    if budget >= 500:
        print("Luxury")
    elif  budget >= 200:
        print("Good")
    elif budget > 0:
        print("Budget friendly")
    else:
        print("Invalid budget")
    
    days=int(input("Enter the number of days \n"))
    totalCost=days*budget

    print(f"""
    days = {days} \n
    budget = {budget} \n
    total cost = {totalCost}""")

except ValueError:
    print("Invalid input. Please enter a valid number")