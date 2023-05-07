from collections import deque


s = deque(input())

res = ''
d = {'(': ')', '[': ']'}
i = 0
while i < len(s)-1:
    if s[i] in d:
        res += s[i] + d[s[i]]
        s.popleft()
    i += 1

print(res)
