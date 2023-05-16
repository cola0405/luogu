# 重复dp

n = int(input())
w = list(map(int, input().split()))

dp = [0]*(int(1e5)+1)
dp[0] = 1
for i in range(n):
    for j in range(w[i],len(dp))[::-1]:
        if dp[j-w[i]] == 1:
            dp[j] = 1

# 太厉害了。。。
# 反过来用j+w[i]再dp一遍，即表示是否有w[i]可以补上的空档
for i in range(n):
    for j in range(1,len(dp)-w[i]):
        if dp[j+w[i]] == 1:
            dp[j] = 1

print(dp.count(1)-1)