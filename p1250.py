# 受限于python 1.2s

n = int(input())
h = int(input())

reqs = []
ans = 0
for i in range(h):
    req = tuple(map(int, input().split()))
    reqs.append(req)

def end_pos(item):
    return item[1]
reqs.sort(key=end_pos)
a = [0]*(n+1)
for req in reqs:
    b,e,t = req
    i = b
    while i<=e and t>0:
        if a[i] == 1:
            t -= 1
        i += 1
    if t==0:
        continue
    i = e
    while i>=b and t>0:
        if a[i] == 0:
            a[i] = 1
            ans += 1
            t -= 1
        i -= 1

print(ans)