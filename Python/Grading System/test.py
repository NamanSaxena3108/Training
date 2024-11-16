names = []
scores = {}

def take_input():
    while True:
        temp_name = input("Enter Name:\n")
    else:
        names.append(temp_name)
        marks = input("Enter the marks by space").split()
        marks = list(map(int, marks))
        scores[temp_name] = marks

def  avg(scores):
    return sum(scores)/len(scores)

def grade(avg):
    if 90 < avg <= 100:
        return "A"
    elif 70 < avg <= 90:
        return "B"
    else:
        return "FAIL"

def output():
    for name in names:
        scores[name] 
        avg = avg(scores[name])
        grade = grade(avg)
        print(f"The grade of {name} is {grade}")
