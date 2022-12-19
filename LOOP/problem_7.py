# g.	1 * 3 * 4 + 2 * 5 * 6 + 3 * 7 * 8 + . . . . + n1 * n2 * n3

n = int(input())
sum = 0
j = 3
for i in range(1, n+1):
    sum += i*j*(j+1)
    j += 2
    
print(sum)
