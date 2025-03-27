size_of_group = int(input())
if size_of_group <= 500:
    if size_of_group % 6 == 0:
        total_block = size_of_group // 6
    else:
        total_block = size_of_group // 6 + 1
    print(total_block)
else:
    exit