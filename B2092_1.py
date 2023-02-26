n = int(input())

lst = list(range(0,n+1))
flags = [1]*n
for i in range(1, n+1):
    p = 1
    t = i
    while t<=n:
        flags[t] *= -1
        p += 1
        t = i*p

for i in range(1, n+1):
    if flags[i] < 0:
        print(i, end=" ")