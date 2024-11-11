class Items:
    def __init__(self,name,price,quantity):                                                              
        self.namePermanent = name
        self.pricePermanent = price
        self.quantityPermanent = quantity

    def display(self):
        print(f'''name - {self.namePermanent} \n
price - {self.pricePermanent} \n
quantity - {self.quantityPermanent}''')
        
class Inventory:

    def __init__(self):
        self.items=[]

    def addItems(self,name,price,quantity):
        for item in self.items:
            if item.name == name:
                print(f" {name} already exists. Please use update_quantity to modify details.")
                return None
        self.items.append(Items(name, price, quantity))

    def update_quantity(self,name,quantity):
        for item in self.items:
            if item.name == name:
                item.quantity = item.quantity + quantity
                print("Quantity updated.") 
            else:
                print("Item not present.")

    def update_price(self):
        pass
    def displayItems(self):
        pass

inventory1 = Inventory()
inventory2 = Inventory()

inventory1.update_quantity("pen", 10)
inventory1.addItems('pen', 100, 15)
# inventory1.addItems('pencil', 5, 100)
# inventory1.addItems('scale', 5, 100)
# inventory1.addItems('Box', 250, 40)