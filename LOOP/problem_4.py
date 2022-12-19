# d.	1+1/2+1/3+ . . . . +1/N

n = int(input())
div= 0
for i in range(1, n+1):
    div += 1/i

print(div) 