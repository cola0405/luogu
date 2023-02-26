n = int(input())

lst = list(map(int, input().split()))

hp = 0
min_hp = 0
for num in lst:
    hp += num
    min_hp = min(hp, min_hp)

print(abs(min_hp) + 1)