T,M = map(int, input().split())

herb = []
for _ in range(M):
    t, v = map(int, input().split())
    herb.append((t,v))

# 当前时间能够采得得最大数量
dp = [0]*(T+1)
for item in herb:
    for i in range(T+1)[::-1]:  # 从右往左才不会重复采药
        if i >= item[0]:
            dp[i] = max(dp[i-item[0]]+item[1], dp[i])

print(dp[T])