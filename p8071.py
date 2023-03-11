H,M = map(int, input().split())

minutes = H*60 + M
minutes -= 45

h = minutes//60
m = minutes%60

print(abs(h), m)