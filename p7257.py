def flip(num):
    return int(num[::-1])

a, b = map(flip, input().split())
print(max(a,b))