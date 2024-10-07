def getQuantity():
    while True:
        try:
            quantity=int(input("Enter the quantity of item :"))
            if quantity<=0:
                print("Quantity should be greater than zero")
            else:
                return quantity
        except ValueError:
            print("Invalid quantity. Enter Again:")

def main():
    items=['Apple','Mosambi','Anar','Aam']
    prices={'Apple':20 , "Anar" : 33.5 , "Aam" :45.7 , 'Anar' : 40 , 'Mosambi':22.8}
    cart={}
    print("Welcome to the shopping cart application")
    print("Available items")
    while True:
        for element in items:
            print(element)
        choice=input("Enter the item name :").capitalize()
        if choice == 'Done':
            break
        elif choice in items:
            quantity=getQuantity()
            if choice in cart:
                cart[choice]=cart[choice]+quantity
            else:
                cart[choice]=quantity
            print("item added to cart!")
    print(cart)
main() 
        