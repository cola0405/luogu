dislike = list(map(int, input().split()))[1:]
m = int(input())

pizza = []
for i in range(m):
    pizza.append(list(map(int, input().split()))[1:])

ans = 0
for p in pizza:
    for item in dislike:
        if item in p:
            break
    else:
        ans += 1

print(ans)

