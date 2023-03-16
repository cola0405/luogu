H, M = map(int, input().split())

minutes = H*60+M - 45

h = minutes//60
m = abs(minutes)%60

if minutes < 0:
    h = 23

print(h, m)

