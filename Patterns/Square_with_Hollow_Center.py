numbers = int(input())
for i in range(1, numbers + 1):
    print("*", end="")
print()
for j in range(numbers - 2):
    print('*' + ' ' * (numbers - 2) + '*')

for i in range(1, numbers + 1):
    print("*", end="")

n=5

output

*****
*   *
*   *
*   *
*****

