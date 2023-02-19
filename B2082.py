b, e = map(int, input().split())

cnt = 0

for i in range(b, e+1):
    while i>0:
        if i%10 == 2:
            cnt += 1
        i //= 10

print(cnt)
