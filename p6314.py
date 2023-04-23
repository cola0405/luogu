def remove_pair():
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if total - (nums[i] + nums[j]) == 100:
                p1 = nums[i]
                p2 = nums[j]
                nums.remove(p1)
                nums.remove(p2)
                return

nums = []
for i in range(9):
    nums.append(int(input()))

total = sum(nums)
remove_pair()
for num in nums:
    print(num)