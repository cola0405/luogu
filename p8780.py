a,b,n = map(int, input().split())

amount = a*5 + b*2
ans = n//amount * 7
n = n%amount

i = 1
while i <= 7 and n>0:
    if i<=5:
        n -= a
    else:
        n -= b
    ans += 1
    i += 1

print(ans)

