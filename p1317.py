n = int(input())

h = list(map(int , input().split()))

ans = 0
down = 0
for i in range(n-1):
    if h[i] > h[i+1]:
        down = 1
    elif h[i] < h[i+1] and down == 1:
        ans += 1
        down = 0

print(ans)
