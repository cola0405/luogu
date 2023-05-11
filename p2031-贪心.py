# 有则马上取 —— 贪心
# 如果有剩余，则合并倒数第一个字串就行
s = input().strip()     # emm。。数据有问题，得要strip
n = int(input())
d = [input().strip() for _ in range(n)]

ans = 0
t = ''
for i in range(len(s)):
    t += s[i]
    for item in d:
        if item in t:
            ans += 1
            t = ''
            break

print(ans)

"""
asdsd
2
a
ds
"""