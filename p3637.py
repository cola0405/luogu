n = int(input())
nums = list(map(int, input().split()))

dp = [1]*n  # dp[i] 表示以当前nums[i]结尾的最长序列
for i in range(n):
    for j in range(i)[::-1]:
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))