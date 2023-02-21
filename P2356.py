# 一个格子上可能有多个敌人，不能简单+1
# 如果每个都去横竖查看的话，会超时的

n = int(input())

row_count = []
column_count = [0]*n
points = []
for i in range(n):
    line = list(map(int, input().split()))
    row_count.append(sum(line))

    for j in range(n):
        column_count[j] += line[j]
        if line[j] == 0:
            points.append((i,j))

ans = -1
for point in points:
    i, j = point
    amount = row_count[i] + column_count[j]
    ans = max(amount, ans)

if ans == -1:
    print("Bad Game!")
else:
    print(ans)