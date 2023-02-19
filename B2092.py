n = int(input())

lst = list(range(0,n+1))
for i in range(1, n+1):
    p = 1
    t = i
    while t<=n:
        lst[t] *= -1
        p += 1
        t = i*p

for i in range(1, n+1):
    if lst[i] < 0:
        print(i, end=" ")