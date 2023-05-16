n = int(input())
nums = list(map(int, input().split()))

max_sum = nums[0]
s = nums[0]
for i in range(1,n):
    s += nums[i]
    max_sum = max(s, max_sum)  # 不能放在s=0后面
    if s <= 0:  # 如果之前累加的是负数，那还不如直接重新开始
        s = 0

print(max_sum)