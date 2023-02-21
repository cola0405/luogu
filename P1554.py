m,n = map(int, input().split())

res = [0]*10
for num in range(m, n+1):
    while num > 0:
        digit = num%10
        res[digit] += 1
        num//=10

for num in res:
    print(num, end=" ")