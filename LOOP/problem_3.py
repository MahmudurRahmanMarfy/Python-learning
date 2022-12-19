# c.	22 * 42 * 62 * . . . . * N2

n = int(input())
sum = 1

for i in range(1, n+1):
    if i%2 == 0:
        sum *= i**2

print(sum)