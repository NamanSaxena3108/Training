seats = [[0 for _ in range(10)] for _ in range(5)]
def book(row,column):
    if seats[row-1][column-1]:
        print("Seat already booked")
    else:
        seats[row-1][column-1] = 1
        print("Seat booked")
        
def check(row,column):
    if seats[row-1][column-1]:
        print('Booked')
    else:
        print('Available')
        
def cancle(row,column):
    if seats[row-1][column-1]:
        seats[row-1][column-1] = 0
        print('Booking cancelled')
    else:
        print('Seat not booked')
        
def total():
    total = 0
    for row in range(5):
        for column in range(10):
            if seats[row][column]:
                if row < 3:
                    total += 500
                else:
                    total += 300
    print(total)
    
def main():
    n = int(input())
    if 1 <= n <= 50:
        for _ in range(n):
            block = input().split()
            operation = block[0]
            if operation == 'BOOK':
                row = int(block[1])
                column = int(block[2])
                book(row,column)
            elif operation == 'CHECK':
                row = int(block[1])
                column = int(block[2])
                check(row,column)
            elif operation == 'CANCEL':
                row = int(block[1])
                column = int(block[2])
                cancle(row,column)
            elif operation == 'TOTAL':
                total()
    else:
        exit
        
main()