def get_target_amount(block, target):
    from itertools import combinations
    ans = 0
    for num in range(1, len(block)+1):
        for item in combinations(block, num):
            if sum(item) == target:
               ans += 1
    return ans


def main():
    n = int(input())
    nums = list(range(1, n + 1))
    if sum(nums) % 2 != 0:
        print(0)
        return

    target = sum(nums) // 4

    block1 = nums[:n//2+1]
    block2 = nums[n//2+1:]

    amount1 = get_target_amount(block1, target)
    amount2 = get_target_amount(block2, target)

    print(amount1+amount2)

main()