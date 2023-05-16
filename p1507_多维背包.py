max_v,max_m = map(int, input().split())
n = int(input())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(max_v+1) for _ in range(max_m+1)]

for item in items:
    v,m,k = item
    for i in range(m, max_m+1)[::-1]:
        for j in range(v, max_v+1)[::-1]:  # 多维背包开多维
            dp[i][j] = max(dp[i-m][j-v] + k, dp[i][j])

print(dp[-1][-1])


