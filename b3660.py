t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    if 0 in cards:
        print('yes')
    else:
        print('no')
