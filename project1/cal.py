print("Enter a first num: ")
x = int(input())
print("Enter a sec num: ")
y = int(input())

print("for addition press 1")
print("for subtraction press 2")
print("for multiply press 3")
print("for divide press 4")

a=int(input())
def cal(n):
    switch={
        1: add(x, y),
        2: sub(x, y),
        2: mul(x, y),
        2: div(x, y)
    }  
    return switch.get(n, "invalid") 

def add(x, y):
    print(x+y)
    exit()

def mul(x, y):
    print(x*y)
    exit()

def sub(x, y):
    print(x-y)
    exit()

def div(x, y):
    if y==0:
        print("invalid")
    else:
        print(x/y)
        
    exit()

cal(a)