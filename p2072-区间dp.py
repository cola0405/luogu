# 贪心 + 区间dp

n,m,k = map(int, input().split())
s = list(map(int, input().split()))

religion = set()
group = 1
for i in range(n):
    religion.add(s[i])
    if len(religion) > k:
        group += 1
        religion = {s[i]}

print(group)


# init danger(i,j)
amount = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    religion = set()
    cnt = 0
    for j in range(i, n+1):
        if s[j-1] not in religion:
            religion.add(s[j-1])
            if len(religion) > k:
                religion = {s[j-1]}
            cnt += 1
        amount[i][j] = cnt

# dp
dp = [float('inf')]*(n+1)
dp[0] = 0   # necessary
dp[1] = 1
for i in range(2, n+1):  # dp[i]用来记录i之前的最低危险值
    for j in range(1, i+1):  # 借助amount数组来dp+模拟后半段(j,i)
        if amount[j][i] <= k:
            dp[i] = min(dp[i], dp[j-1]+amount[j][i])

print(dp[n])

"""
7 4 3
1 2 3 1 1 1 3
"""