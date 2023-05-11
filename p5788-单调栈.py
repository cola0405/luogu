# 单调栈
n = int(input())
nums = list(map(int, input().split()))

ans = []
s = []
for i in range(n)[::-1]:
    while len(s)>0 and nums[s[-1]] <= nums[i]:
        s.pop()
    if len(s) == 0:
        ans.append(0)
    else:
        ans.append(s[-1]+1)
    s.append(i)

print(' '.join(map(str, ans[::-1])))