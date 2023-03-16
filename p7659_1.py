p = []
for i in range(8):
    p.append(int(input()))

p = p*2

ans = 0
for i in range(8):
    tmp = sum(p[i:i+4])
    ans = max(tmp, ans)

print(ans)