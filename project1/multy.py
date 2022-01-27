# print("enter a number: ")
# n = int(input())

# for j in range(1, n+1):
#     for i in range(1,11):
#         mul = j * i
#         print(f"{j} * {i} = {mul}")
#     print('\r')

print([x*2 for x in range(1,11)])
class Person:
    fName = "Bhargav"
    lName = "Sonagara"
    def __init__(self, name, age):
      self.fname = name
      self.age = age
    

bhargav = Person()
print(bhargav) 