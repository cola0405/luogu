n,m,k = map(int, input().split())

religions = list(map(int, input().split()))

# min group
group = 0
count = 0
tmp = set()
for religion in religions:
    tmp.add(religion)
    if len(tmp) == 3:
        group += 1
        tmp.clear()
if len(tmp) != 0:
    group += 1

# min danger

# build danger
danger = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    tmp = set()
    for j in range(i,n+1):
        tmp.add(religions[j-1])
        danger[i][j] = len(tmp)

# build dp
dp = [float('inf')]*(n+1)  # dp[i] 表示i之前的最小的危险值
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(danger[j][i-1]+dp[i], dp[i])