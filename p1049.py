v = int(input())
n = int(input())

items = [int(input()) for _ in range(n)]

# 当前空间大小最多放多少物品
dp = [0]*(v+1)
for item in items:
    for i in range(v+1)[::-1]:
        if i >= item:
            dp[i] = max(dp[i-item]+item, dp[i])

print(v - dp[v])

