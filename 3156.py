n,m = map(int, input().split())
ids = list(map(int, input().split()))
ask = list(map(int, input().split()))

for num in ask:
    print(ids[num-1])