# e.	1 - 2 + 3 - 4 + 5 - 6 + . . . . + N

n = int(input())
sum = 0
for i in range(1, n+1):
    if i%2 == 0:
        sum -= i
    else:
        sum += i

print(sum)