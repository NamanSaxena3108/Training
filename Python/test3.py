no_of_choco = int(input())
if no_of_choco < 300:
    no_of_box= 0
    if no_of_choco % 12 == 0:
        number_of_box_needed = no_of_choco // 12
    else:
        number_of_box_needed = no_of_choco // 12 + 1
    print(number_of_box_needed)
else:
    exit