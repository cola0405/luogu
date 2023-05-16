n = int(input())
profit = [int(input()) for _ in range(n)]

max_profit = profit[0]  # 这种题一般不允许初始化为0
s = 0
for i in range(n):
    s += profit[i]
    max_profit = max(s, max_profit)
    if s < 0:
        s = 0

print(max_profit)