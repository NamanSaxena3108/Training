invetory ={}

def add(name,quantity,price):
    if name in invetory:
        print('Item already exists')
    else:
        if 1 <= quantity <= 1000 and 0.01 <= price <= 10000:
            invetory[name] = {'quantity':quantity,'price':price}
            print("Item added successfully")
        else:
            exit
            
def update(name,quantity):
    if name not in invetory:
        print("Item not found")
    else:
        if 1 <= quantity <= 1000:
            invetory[name]['quantity'] += quantity
            print("Quantity updated")
        else:
            exit
            
def delete(name):
    if name not in invetory:
        print("Item not found")
    else:
        del invetory[name]
        print("Item deleted")
        
def total():
    total = 0
    for item in invetory:
        total += invetory[item]['quantity']*invetory[item]['price']
    print(f"{total:.2f}")

def main():
    n = int(input())
    if 1<= n <= 1000:
        for _ in range(n):
            block = input().split()
            operation = block[0]
            if operation == 'ADD':
                name = block[1]
                quantity = int(block[2])
                price = float(block[3])
                add(name,quantity,price)
            elif operation == 'UPDATE':
                name = block[1]
                quantity = int(block[2])
                update(name,quantity)
            elif operation == 'DELETE':
                name = block[1]
                delete(name)
            elif operation == 'TOTAL':
                total()
    else:
        exit
            
main()  