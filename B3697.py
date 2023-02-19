a,b,c = map(int, input().split())

if a%c == 0 and b%c == 0:
    print(a//c * b//c)
else:
    print(-1)