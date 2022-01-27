def myFunction(input_list:list):
    input_list.sort()
    dict_a={}
    for word in input_list:
        lista = word[0].lower()
        if not lista in dict_a:
            dict_a[lista] = [word]
        else:
            dict_a[lista].append(word)
        
        
        
    print(dict_a)
        
    
    
    
myFunction(['Ben', 'bakru', 'Alif', 'Alice'])


def capital_indexes(word):
    lista= [x for x,y in enumerate(word) if y.isupper()]  
    print(lista)
capital_indexes("HeLLP io12")
    

filename = "bhargav.java"
ext = filename.split(".")
print(ext[-1])
print(type(ext[-1]))

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])


def num(n):
    n2 = n*10+n
    n3 = n*100 + n*10 + n
    result = n + n2 + n3
    return result
print(num(5))

num=lambda x : x+x*10+x+x*100+x*10+x
print(num(5))

class Dog:
    def __init__(self, attr1, attr2) -> None:
        self.attr1 = attr1
        self.attr2 = attr2
    def show(self):
        print(self.attr1)
        return(self.attr2)

obj1=Dog("dog", "mamal")
print(obj1.attr1)
print(obj1.show())

class Bhargav:
    def __init__(self, jai = "gav") -> None:
        self.bhar = "bhargav"
        self.jai = jai
    
    def show(self):
        print(self.bhar)
        print(self.jai)

obj1 = Bhargav("jai")
obj1.show()

class Adition:
    first = 0
    second = 0
    additon = 0
    def __init__(self, f, s) -> None:
        self.first = f    
        self.second = s    
    
    def display(self):
        print("First number is: ", self.first)
        print("Second number is: ", self.second)
        print("Addition number is: ", self.additon)
    
    def calc(self):
        self.additon = self.first + self.second
    
obj1 = Adition(100, 2000)
obj1.calc()
obj1.display()

class Employee:
    def __init__(self) -> None:
        print("1")
    
    def __del__(self):
        print("2")
    
def cal():
    print("5")
    obj = Employee()
    print("3")
    return obj

obj = cal()
print("4")


class Person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname
    
    def prints(self):
        print(self.firstname, self.lastname)
    
class Student(Person):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)
        self.graduation = 2022

obj1 = Student("Bhargav", "Sonagara")
obj1.prints()
print(obj1.graduation)

class Person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname
class Student(Person):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.graduation = year
        
    def welcome(self):
        print(f"Hi {self.firstname} {self.lastname} you pass out in {self.graduation}")

obj1 = Student("bhargav", "sonagara", "2022")
obj1.welcome()
        
            
