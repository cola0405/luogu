m = int(input())
n = int(input())

nums = list(map(int, input().split()))

count = 0
for num in nums:
    if m-num >= 0:
        m -= num
        count += 1

print(n-count)