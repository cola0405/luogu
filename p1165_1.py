# 冗余最大值

n = int(input())

max_weight = [0]
repo = []
for _ in range(n):
    command = list(map(int, input().split()))
    if len(command) == 2:
        repo.append(command[1])
        cur_weight = max(command[1], max_weight[-1])
        max_weight.append(cur_weight)

    if command[0] == 1 and len(repo) > 0:
        item = repo.pop()
        max_weight.pop()

    if command[0] == 2:
        print(max_weight[-1])