n = int(input())

ans = 0
cards = ["X", "J", "Q", "K", "A"]

s = ''
for i in range(n):
    s += input()

for i in range(len(cards)):
    ans += s.count(cards[i])*i

print(ans)

