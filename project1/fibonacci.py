#fibonacci

x = int(input())
a=0
b=1
if x==1:
    print(a)
elif x==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for y in range(x-2):
        c=a+b
        a=b
        b=c
        print(c)
