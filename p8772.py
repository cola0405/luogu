n = int(input())

lst = list(map(int, input().split()))

ans = 0
total = sum(lst)
for num in lst:
    ans += num * (total-num)

print(ans//2)