# f.	1 * 2 + 2 * 3 + 3 * 4 + . . . . + n1 * n2

n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i*(i+1)

print(sum)