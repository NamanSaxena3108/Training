#' '
#" "
#''' '''
#""" """ 
name=input("Hello User: Please Enter your name \n")

print("Welcome to the class 3A "+name)

message='Hello '+name+' Welcome to Personalized Adventure Guide'
print(message)

message='Hello {var} Welcome to Personalized Adventure Guide'.format(var=name)
print(message)

print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")

