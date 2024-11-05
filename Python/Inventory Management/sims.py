class Items:
    def __init__(self,name,price,quantity):                                                              
        self.namePermanent = name
        self.pricePermanent = price
        self.quantityPermanent = quantity

    def display(self):
        print(f'''name - {self.namePermanent} \n
price - {self.pricePermanent} \n
quantity - {self.quantityPermanent}''')
        
i1=Items("pen",20,200)
i2=Items("pencil",50,300)
i3=Items("file",50,150)
i4=Items("scale",20,100)

items=[i1,i2,i3,i4]

class Inventory:
    def __init__(self):
        items=[]
    def addItems(self,name,price,quantity):
        items.__add__(Items(name,price,quantity))
    def update_quantity(self):
        pass
    def update_price(self):
        pass
    def displayItems(self):
        pass

inventory1=Inventory()
inventory1.addItems()
inventory1.addItems()
inventory1.addItems()
inventory1.addItems()