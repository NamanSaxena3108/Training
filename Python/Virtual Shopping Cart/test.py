def getQuantity():
    while True:
        try:
            quantity=int(input("Enter the quantity of the item: \n"))
            if quantity<0:
                print("Quantity must be positive :")
            else:
                return quantity
        except ValueError:
            print("Invalid Quantity.Please enter a positive integer :")

def items(quantity,prices):
    for i in quantity:
        for j in prices:
            if i == j:
                print(f"{i} is for sale at price {prices[j]}")

def check_available(quantity,item_quantity,item_name):
    for i in quantity:
        if i == item_name:
            if quantity[i] > item_quantity:
                quantity[i]-=item_quantity
                return True
            else:
                return False
        else:
            print("Enter the correct choice")
            return False

def cart(quantity):
    cart={}
    while True:
        try:
            item_name=input("Enter the name of item you want to add \n").capitalize()
            item_quantity=getQuantity()
            check=check_available(quantity,item_quantity,item_name)
            if check == True:
                cart[item_name]=item_quantity
                ans=input("Want to add more item ?\n").lower()
                if ans == 'yes':
                    continue
                elif ans == 'no':
                    return cart
                else:
                    print("Enter correct choice")
                    continue
            else:
                print("Item is not available")
        except Exception as e:
            print(e)

def remove_items(cart,ans):
    while True:
        try:
            item_to_remove=input("Enter the item to remove \n").capitalize()
            for i in cart:
                if i == item_to_remove:
                    del cart[i]
                    print("item is removed")
                else:
                    print("Enter valid item name")
                ans=input("Want to remove more item ?\n").lower()
                if ans == 'yes':
                    continue
                elif ans =='no':
                    return cart
                else:
                    print('Enter Correct choice')
                    continue
        except Exception as e:
            print(e)

def checkout(car,prices):
    tot_amount=0
    total=0
    for i in car:
        for j in prices:
            if i==j:
                tot_amount=car[i]
                total+=tot_amount*prices[j]
    return total

def display_cart_items(car):
    for i in car:
        print(f"{i} : {car[i]}")

def reduce_item(car):
    while True:
        try:
            ans=int(input("Enter the quantity to remove \n"))
            for i in car:
                c=car[i]
                temp=c-ans
                car[i]=temp  
            ans1=input("Want to remove more item ?\n").lower()
            if ans1 == 'yes':
                continue
            elif ans1 =='no':
                return cart
            else:
                print('Enter Correct choice')
                continue
        except Exception as e:
            print(e)
        
def main():
    print("Welcome to the virtual shopping cart \n")
    quantity={'Apple':50 , "Anar" : 50 , "Aam" :50 , 'Mosambi':50}
    prices={'Apple':20 , "Anar" : 33.5 , "Aam" :45.7 , 'Anar' : 40 , 'Mosambi':22.8}
    items(quantity,prices)
    car=cart(quantity)
    print(car)
    ans=input("Do you want to remove a item from the cart? or reducing the quantity enter reduce\n").lower()
    if ans == 'yes':
        remove_items(car,ans)
    elif ans =='reduce':
        reduce_item(car)
    amount=checkout(car,prices)
    display_cart_items(car)
    print(f"Amount to be paid {amount}")
main()