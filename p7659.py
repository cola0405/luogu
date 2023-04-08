p = []
for i in range(8):
    p.append(int(input()))

ans = 0
for i in range(8):
    tmp = 0
    for j in range(4):
        tmp += p[(i+j)%8]
    ans = max(tmp, ans)
print(ans)

