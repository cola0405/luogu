n = int(input())
price = []
for i in range(n):
    price.append(int(input()))

price.sort()
i = len(price)-1
cost = 0
while i>=2:
    cost += price[i] + price[i-1]
    i -= 3

while i >= 0:
    cost += price[i]
    i -= 1

print(cost)
