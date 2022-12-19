# h.	1 + 5 + 9 + . . . . + Nth number

n = int(input())
sum = 0
j = 1
for i in range(1, n+1, 4):
    sum += i
print(sum)