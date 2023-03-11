n = int(input())
t = list(map(int, input().split()))

i = 0
ans = 1
cnt = 1
while i+1 < n:
    if t[i+1] > t[i]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1
    i += 1
ans = max(cnt, ans)
print(ans)