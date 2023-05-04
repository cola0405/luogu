l, n = map(int, input().split())

re_amount = 0
tree = [-1]*(l+1)
for _ in range(n):
    op, start, end = map(int, input().split())

    for i in range(start, end+1):
        if tree[i] == 1 and op == 0:
            re_amount += 1

        # ps 如果已经种了树，则不会再种树苗
        if (tree[i] == -1 and op == 0) or tree[i] != -1:
            tree[i] = op

remain = tree.count(1)
print(remain)
print(re_amount)