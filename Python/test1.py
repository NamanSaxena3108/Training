number_of_apples = int(input())
number_of_box_needed = 0
if number_of_apples % 10 == 0:
    number_of_box_needed = number_of_apples // 10
else:
    number_of_box_needed = number_of_apples // 10 + 1
print(number_of_box_needed)