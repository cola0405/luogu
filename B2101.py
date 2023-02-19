m,n = map(int, input().split())

ans = 0
for i in range(m):
    line = list(map(int, input().split()))
    if i == 0 or i == m-1:
        ans += sum(line)
    else:
        ans += line[0] + line[-1]

print(ans)

