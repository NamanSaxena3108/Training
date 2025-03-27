amt_of_water_requested = int(input())
if amt_of_water_requested <= 10000:
    if amt_of_water_requested % 1000 == 0:
        min_jugs = (amt_of_water_requested//1000)
    else:
        min_jugs = (amt_of_water_requested//1000)+1
    print(min_jugs)
else:
    exit