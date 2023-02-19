l, n = map(int, input().split())

trees = [1]*(l+1)
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

for a in area:
    for j in range(a[0], a[1]+1):
        trees[j] = 0

ans = 0
for i in trees:
    if i == 1:
        ans += 1

print(ans)
