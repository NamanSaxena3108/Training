class Student:
    def __init__(self,name):
        self.name = name

    def take_marks(self,n):
        L = []
        for i in range(n):
            mark = int(input("Enter mark:"))
            L.append(mark)
        return L
    
    def calculate_average(self,L):
        return sum(L)/len(L)
    
    def grades(self,tot):
        ave = self.calculate_average(self.take_marks(tot))
        if ave >= 90 :
            return 'A'
        elif ave >= 80 :
            return 'B'
        elif ave >= 70 :
            return 'C'
        elif ave >= 60 :
            return 'D'
        else:
            return 'F'
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Grade : {self.grade}")

students = []
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    student_name = input("Enter student name: ")
    S = Student(student_name)
    tot_sub = int(input("Enter the number of subjects : "))
    grade = S.grades(tot_sub)  
    S.grade = grade
    students.append(S) 

for student in students:
    student.display_details()

print(students)