n = int(input())

ans = 0
nums = []
for num in range(2,n):
    ans += num
    nums.append(num)
    if ans > n:
        break
nums.remove(ans - n)

ans = 1
for num in nums:
    ans*=num

res = " ".join(map(str, nums))
print(res)
print(ans)
