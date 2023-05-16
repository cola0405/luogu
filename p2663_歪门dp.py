# 选若干个，最大值

n = int(input())
score = [int(input()) for _ in range(n)]
half = sum(score)//2

# 表示dp[i][j] 表示选i个人是否能够达到j分
dp = [[0]*(half+1) for _ in range(n//2+1)]

# init dp
dp[0][0] = 1

for i in range(n):
    for j in range(1, n//2+1)[::-1]:
        for k in range(score[i], half)[::-1]:
            if dp[j-1][k-score[i]] == 1:
                dp[j][k] = 1

for i in range(half)[::-1]:
    if dp[-1][i] == 1:
        print(i)
        break