p = []
for i in range(8):
    p.append(int(input()))
p += p[:4]

ans = 0
for i in range(8):
    ans = max(sum(p[i:i+4]), ans)
print(ans)

