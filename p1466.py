def main():
    n = int(input())
    nums = list(range(1, n + 1))
    if sum(nums) % 2 != 0:
        print(0)
        return

    target = sum(nums) // 2

    # 和为 i 的方案数
    dp = [0]*(target+1)
    # 和为 0 的方案数 -- 用于后续dp出dp[1]
    dp[0] = 1

    # 模拟依次放入n个数字 -- 利用dp的记录功能 -- access用j-i
    for i in range(1, n+1):
        for j in range(i, target+1)[::-1]:
            dp[j] += dp[j-i]

    # dp[3]=2指的是可选{1,2}、{3} 但其实只算是一种分法 -- {1,2} | {3}
    print(dp[-1]//2)
main()