def totalCost(budget,duration):
    return budget*duration

def getValidNumber(prompt):
    while True:
        try:
            value=input(prompt)
            return value
        except ValueError:
            print("Invalid Input! Enter again")

def Location(destination):
    destination=str(destination).lower().strip()
    if destination == "mountain":
        print("You are going to the Mountain")
    elif destination == "beach":
        print("You are going to the Beach")
    else:
        print("Enter the correct choice")

def Amount(budget):
    if budget >= 500:
        print("Luxury")
    elif  budget >= 200:
        print("Good")
    elif budget > 0:
        print("Budget friendly")
    else:
        print("Invalid budget")

def Printing(duration,budget,total):
    print(f""" \nNo. of Days are : {duration} \n
Your Budget was : {budget} \n
Your Total Expenditure will be : {total}""")


name=input("Hello User 😊 Please Enter Your Name \n")
print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")
destination=getValidNumber("Where do you want to go : ")
Location(destination)
budget=int(getValidNumber("Enter the Budget : "))
Amount(budget)
duration=int(getValidNumber("Enter the Number of days : "))
total=totalCost(budget,duration)
Printing(duration,budget,total)
