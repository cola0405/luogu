n = int(input())
t = list(map(int, input().split()))

ans = 1
cnt = 1
for i in range(n-1):
    if t[i+1] > t[i]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1
ans = max(cnt, ans)
print(ans)

