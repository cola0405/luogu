# 最值链

n = int(input())

max_chain = {0: 0}
repo = []
max_weight = 0
for _ in range(n):
    command = list(map(int, input().split()))
    if len(command) == 2:
        repo.append(command[1])
        if command[1] > max_weight:
            max_chain[command[1]] = max_weight
            max_weight = command[1]

    if command[0] == 1 and len(repo) > 0:
        item = repo.pop()
        if item == max_weight:  # get second max weight
            temp = max_weight
            max_weight = max_chain[max_weight]
            max_chain.pop(temp)

    if command[0] == 2:
        print(max_weight)