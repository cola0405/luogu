m = int(input())

l = 1
res = l
for r in range(2, m//2+2):
    res += r
    while res > m:
        res -= l
        l += 1
    if res == m:
        print(l, r)