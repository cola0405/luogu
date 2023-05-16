# 贪心
# 如果有剩余，则合并倒数第一个字串就行
s = input().strip()
n = int(input())

words = [input().strip() for _ in range(n)]
# 不进行排序不会有问题，因为不会错过
# 但是排序后效率相对会更高
# words.sort(key=lambda item: len(item))

count = 0
cur = ''
for c in s:
    cur += c
    for word in words:
        if word in cur:
            count += 1
            cur = ''
            break

print(count)