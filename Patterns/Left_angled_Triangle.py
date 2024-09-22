number = int(input())

for i in range(number+1,0,-1):
    for j in range(i-1):
        print("*", end="")
    print()

n=5

output:

*****
****
***
**
*
