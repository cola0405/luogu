def flip(num):
    return int(str(num)[::-1])

a, b = map(int, input().split())

a = flip(a)
b = flip(b)

print(max(a,b))

