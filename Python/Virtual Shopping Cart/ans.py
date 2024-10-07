# #print value of a list in new line in a single line code
# items=['apple','Mosambi','Anar','Aam0']
# print(*items,sep='\n')
# #add to number with out operator
# x=10
# y=20
# print(x.__add__(y))
# print(x.__sub__(y))
# #insert the element without using methods
# l=[1,2,3]
# element=5
# l[len(l):]=[element]
# print(l)
# #Implementing the concept of append in List
# l=[1,2,3]
# element=int(input("Enter the number to append"))
# l[len(l):]=[element]
# print(l)
# #Implementing the concept of extend in List
# l=[1,2,3]
# l1=[4,5,6]
# l[len(l):]=l1
# print(l)
# #Implementing the concept of insert in List
# l=[1,2,3]
# index=int(input("Enter the index where to insert"))
# element=int(input("Enter the element to insert"))
# l[index:index]=[element]
# print(l)
# #Implementing the concept of append in list in one line
# l=[1,2,3]
# app = lambda l,element : l.__setitem__(slice(len(l),len(l)),[element])
# app(l,5) 
# print(l)
# #Implementing the concept of extend in list in one line
# l=[1,2,3]
# ext = lambda l,element : l.__setitem__(slice(len(l),len(l)),element)
# ext(l,[4,5,6])
# print(l)
# #Implementing the concept of insert in list in one line
# l=[1,2,3]
# ins = lambda l,index,element : l.__setitem__(slice(index,index),[element])
# ins(l,1,100)
# print(l)
