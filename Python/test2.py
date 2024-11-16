no_of_days = int(input())
sales_list = list(map(int,input().split()))
count = 0
avg = sum(sales_list)/len(sales_list)
for sale in sales_list:
    if sale > avg:
        count+=1
print(count)