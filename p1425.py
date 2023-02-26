a,b,c,d = map(int ,input().split())

hour = c-a
minute = 0
if d<b:
    hour -= 1
    print(hour, d+60-b)
else:
    print(hour, d-b)