no_of_student = int(input())
if no_of_student >30:
    exit
else:
    stud_height = list(map(int,input().split()))
    if any(height > 200 for height in stud_height):
        exit
    else:
        count = 0
        avg = sum(stud_height)/len(stud_height)
        for height in stud_height:
            if height > avg:
                count+=1
        print(count)