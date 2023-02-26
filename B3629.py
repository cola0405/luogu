# 规律

n = int(input())

# print(n - (n-1)//3)

if n%3 <= 1:
    print((n//3)*2 + 1)
else:
    print((n//3)*2 + 2)

