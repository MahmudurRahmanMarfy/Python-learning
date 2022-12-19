# b.	1^2 + 3^2 + 5^2 + . . . . + N^2

n = int(input())
sum = 0

for i in range(n+1):
    if not i%2 == 0:
        sum += i**2
print(sum)