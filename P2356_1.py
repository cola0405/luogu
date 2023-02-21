# 一个格子上可能有多个敌人，不能简单+1
# 如果每个都去横竖查看的话，会超时的

n = int(input())

r = []
for i in range(n):
    line = list(map(int, input().split()))
    r.append(line)

row_count = []
column_count = [0]*n

for i in range(n):
    for j in range(n):
        if r[i][j] != 0:
            column_count[j] += r[i][j]
    row_count.append(sum(r[i]))

ans = -1
for i in range(n):
    for j in range(n):
        if r[i][j] == 0:
            amount = row_count[i] + column_count[j]
            ans = max(amount, ans)

if ans == -1:
    print("Bad Game!")
else:
    print(ans)