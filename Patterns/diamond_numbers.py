number = int(input())

for i in range(1,number+1):
    print(' ' * (number - i), end= '')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i-1,0,-1):
        print(j,end= '')
    print()
for i in range (number-1 , 0 , -1):
    print(' ' * (number - i), end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()



