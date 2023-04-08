n = int(input())

types = []
for _ in range(n):
    s = input()
    res = ''
    for i in range(56, 81):
        amount = s.count(chr(i))
        if amount > 0:
            res += chr(i)+str(amount)

    if res not in types:
        types.append(res)

print(len(types))
