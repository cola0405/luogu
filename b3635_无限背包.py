# 无限背包 -- 内外倒转，从左往右即可
n = int(input())

coins = [1,5,11]
dp = [float('inf')]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    for j in range(3):
        dp[i] = min(dp[i-coins[j]] + 1, dp[i])

print(dp[-1])