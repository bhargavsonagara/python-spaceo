import random

print(random.uniform(1,10))
print(random.randint(1,10))

greet = ("hi", "hello", "kese ho", "jeete rho")
print(random.choice(greet) + ' bhargav')
print(random.choices(greet, k=10))

import time

t = time.localtime(time.time())
a=t.tm_sec
print(a) 


ts = int(time.time())
print(ts)
x = int(input())
y = int(input())

if y<x:
    num = ts%(x-y+1)
    num=num+y
    print(num)
else:
    num = ts%(y-x+1)
    num=num+x
    print(num)

