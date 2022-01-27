#List

l = ["my", "name", "is", "khan"]
print(l)

l = ["my", "name", "is", "bhargav", "also"]
print(l)

print(len(l))

print(type(list))

th = list(("hello", 12, "kem", "cho"))
print(th)

for i in th:
    print(i)

th.insert(1, "bhargav")
print(th)

th.append("jai")
print(th)

th.extend(l)
print(th)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)

newlist = []
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist =[]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist.sort()
print(newlist)

newlist.sort(reverse=True)
print(newlist)

#Tuple

t = ("hello", 12, "kem", "cho")
print(t)

sub = 2400
like = 240
com = 24

li = [
    sub>2000,
    like>200,
    com>20
]
if all(li):
    print("Awesome")
    

sub = 2400
like = 240
com = 24

li = [
    sub>2500,
    like>300,
    com>20
]

if any(li):
    print("awesome")

sub = 2400
like = 240

print(sub, like)

sub, like = like, sub #swaping
print(sub, like)

a = [1,2,3,4,4,3,2,1,4,5,6,7,6,7,5,4]
a = list(set(a))
print(a)

a = [2,3,4,4,3,2,1,4,5,6,7,6,7,5,4]
a = max(set(a), key=a.count)
print(a)

odd_square = [x**2 for x in range(1,11) if x%2!=0]
print(odd_square)

def sum(*p):
    result=0
    for i in p:
        result = result + i
    return result
print(sum(2,3,4,5,6))

name = "bhargav sonagara"[::-1]
print(name)

str = "madqam"
isPalin = str.find(str[::-1])==0
print(isPalin)


