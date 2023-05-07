n = int(input())
stone = list(map(int, input().split()))
s = [0]

dp = [[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(n):
    s.append(s[i]+stone[i])

    # init dp
    dp[i+1][i+1] = 0

# 子区间从小到大dp
for length in range(2, n+1):
    for i in range(1, n-length+2):
        j = i+length-1
        for k in range(i, j):   # 枚举分界线
            new_val = dp[i][k] + dp[k+1][j] + (s[j]-s[i-1])
            dp[i][j] = min(new_val, dp[i][j])

print(dp[1][n])



