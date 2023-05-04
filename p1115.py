n = int(input())
nums = list(map(int, input().split()))

ans = nums[0]
s = nums[0]
for i in range(1,n):
    s += nums[i]

    # 不能放在s=0之后
    # 如果数字都是负数，是会出问题的，不能选0个数字
    ans = max(ans, s)

    # s做连续区间累加，一旦s<0 则还不如从0开始
    if s < 0:
        s = 0

print(ans)