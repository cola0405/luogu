n = int(input())

lst = list(map(int, input().split()))

res = 0
min_hp = 0
for num in lst:
    res += num
    min_hp = min(res, min_hp)

print(min_hp*-1 + 1)