a = int(input())

for i in range(a):
    for j in range(i+1):
        print('* ', end="")
    print('\r')

print('\n')
for i in range(a):
    for k in range(a-i-1):
        print(" ", end="")
    for j in range(i+1):
        print('*', end="")
    for l in range(j):
        print('*', end="")
    print('\r')
