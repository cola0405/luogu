p = []
for i in range(8):
    p.append(int(input()))

# make it rounded
for i in range(4):
    p.append(p[i])

ans = 0
for i in range(8):
    tmp = sum(p[i:i+4])
    ans = max(tmp, ans)

print(ans)