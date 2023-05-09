class Node:
    def __init__(self, val):
        self.val = val
        self.last = None
        self.next = None


n = int(input())
head = Node(1)
d = {1: head}

for id in range(2, n + 1):
    k, p = map(int, input().split())
    node = Node(id)
    d[id] = node
    if p == 0:  # deal with insert
        if d[k].last is not None:
            node.last = d[k].last
            node.last.next = node
        d[k].last = node
        node.next = d[k]

        # update head
        if k == head.val:
            head = node
    else:
        if d[k].next is not None:
            node.next = d[k].next
            node.next.last = node
        node.last = d[k]
        d[k].next = node

# remove item
m = int(input())
for _ in range(m):
    id = int(input())
    if id not in d:
        continue

    last = d[id].last
    next = d[id].next

    # update head
    if d[id] == head:
        head = next

    # update connection
    if last is not None:
        last.next = next
    if next is not None:
        next.last = last

    # remove from d -- dealing with repeat delete command
    d.pop(id)

nodes = []
cur_node = head
while cur_node:
    nodes.append(str(cur_node.val))
    cur_node = cur_node.next

print(' '.join(nodes))

'''
4
1 1
2 1
3 1
1
1

'''



