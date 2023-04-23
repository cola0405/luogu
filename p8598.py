n = int(input())
ids = []
for i in range(n):
    ids.extend(list(map(int, input().split())))

ids.sort()

lost = -1
repeat = -1
for i in range(len(ids)-1):
    if ids[i+1] == ids[i]+2:
        lost = ids[i]+1
    if ids[i] == ids[i+1]:
        repeat = ids[i]

print(lost, repeat)

