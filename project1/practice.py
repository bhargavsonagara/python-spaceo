print("Twinkle, twinkle, little star,"+ '\n' + '\t' + " How I wonder what you are!" + '\n' '\t' '\t' + "Up above the world so high, " + '\n' '\t' '\t' +"Like a diamond in the sky. " + '\n' + "Twinkle, twinkle, little star, "+ '\n' '\t' +"How I wonder what you are")

import sys
print(sys.version)
print(sys.version_info)

import time
t = time.localtime(time.time())
print(t.tm_hour)

import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def area(r):
    are = 3.14*r*r
    return are

print("%.2f"%(area(1.3)))

str1 = "Bhargav"
str2 = "Sonagara"

str1, str2 = str2, str1
print(str1, str2)


def sol(n):
    s=0
    for i in range(1, n):
        s = s+2
        yield s

for i in sol(5):
    print(i)

def sqr():
    for i in range(1, 101):
        s = i**2
        yield s
    
for i in sqr():
    print(i)

lista = [1,2,3,4,5,6,7,8,9,0]
newlist = [x for x in lista if x%2!=0]
print(newlist)

newlist = [x if x%2!=0 else 'g' for x in lista]
print(newlist)

#class

class Dog:
    n1 = "male dog"
    n2 = "female dogi"
    def combine(self):
        n3 = self.n1 + self.n2
        print(n3)

obj1 = Dog()
print(obj1.n1)
obj1.combine()

import add
import subtract
import mul
import subtract
import divide
import inputs

def do():
    x, y = inputs.inputs()
    print("for addition press 1")
    print("for subtraction press 2")
    print("for multiply press 3")
    print("for divide press 4")

    a=int(input())
    def cal(n):
        switch={
            1: add.add(x, y),
            2: subtract.sub(x, y),
            3: mul.mul(x, y),
            4: divide.div(x, y)
        }
        
        return switch[n]
    
    print(cal(a))
    
    print("do you want more calculation yes or no: ")
    a = input()
    if a!="yes" and a!="no":
        print("wrong input")
        exit()
    elif a=="yes":
        do()
    else:
        exit()
    

    
