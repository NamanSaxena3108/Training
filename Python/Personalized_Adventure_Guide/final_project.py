def totalCost(budget,duration):
    """Calculate the total cost based  on the days and budget"""
    return budget*duration

def getValidNumber(prompt):
    """This check for any of the input that a user enter should 
    be of Integer Type and doess not match tha test case or our requirement"""
    while True:
        try:
            value=input(prompt)
            if value.isnumeric():
                return value
            else:
                print("Wrong input. Please give input again")
                continue
        except ValueError:
            print("Invalid Input! Enter again")

def getDesti(prompt):
    """Check if the input is in string and is valid for our demand. """
    while True:
        try:
            value=input(prompt)
            if value == "mountain" or value == "Mountain": 
                return value
            elif value == "Beach" or value == "beach":
                return value
            else:
                print("Wrong input. Please give input again")
                continue
        except ValueError:
            print("Invalid Input! Enter again")

def Location(destination):
    """Confirm the Location based on our Input
It also convert our input in lower form and strip all the unecessary spaces"""
    destination=str(destination).lower().strip()
    if destination == "mountain":
        print("You are going to the Mountain")
    elif destination == "beach":
        print("You are going to the Beach")
    else:
        print("Enter the correct choice")

def Amount(budget):
    """Check for the amount that we had enter and according to our budget and provide with needful info"""
    if budget >= 500:
        print("Luxury")
    elif  budget >= 200:
        print("Good")
    elif budget > 0:
        print("Budget friendly")
    else:
        print("Invalid budget")

def Printing(duration,budget,total):
    """It take the value from the other function and print all the necessary information"""
    print(f""" \nNo. of Days are : {duration} \n
Your Budget was : {budget} \n
Your Total Expenditure will be : {total}""")


name=input("Hello User 😊 Please Enter Your Name \n")
print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")
destination=getDesti("Where do you want to go : ")
Location(destination)
budget=int(getValidNumber("Enter the Budget : "))
Amount(budget)
duration=int(getValidNumber("Enter the Number of days : "))
total=totalCost(budget,duration)
Printing(duration,budget,total)
