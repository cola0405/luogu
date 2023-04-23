k = int(input())

coins = 1
day = 0
amount = 0
for i in range(1, k+1):
    amount += coins
    day += 1
    if day == coins:
        coins += 1
        day = 0

print(amount)

