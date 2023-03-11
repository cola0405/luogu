n, k = map(int, input().split())

i = 1
cnt = 0
ans = 0
while i <= n:
    cnt += 1
    if cnt == k:
        ans += 1
        cnt = 1
    ans += 1
    i += 1

print(ans)