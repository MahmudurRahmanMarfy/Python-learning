# i.	1 + 2 + 4 + 5 + 7 + 8 + . . . . + N

n = int(input())
sum = 0
j=1
for i in range(1, n+1):
    if j%3 == 0:
        j+=1
    sum = sum + j
    j+=1
print(sum)
