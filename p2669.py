k = int(input())

ans = 0
coins = 1
day = 1
cnt = 0
while day <= k:
    if cnt == coins:
        coins += 1
        cnt = 0
    ans += coins
    cnt += 1
    day += 1

print(ans)