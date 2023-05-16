# 借助其他数组来帮助dp

s = int(input())

# build factor
factor = [0]*(s+1)
for i in range(1, s//2+1):  # 数
    for j in range(2, s//i+1):  # 倍数，从2开始，排除自身
        factor[i*j] += i

# build dp
dp = [0]*(s+1)
for num in range(2, s+1):  # 放新数
    for i in range(num, s + 1)[::-1]:  # 反复刷
        dp[i] = max(dp[i-num] + factor[num], dp[i])  # 取或者不取

print(dp[-1])