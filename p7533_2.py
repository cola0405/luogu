n = int(input())

ans = [0, 0, 0, 0, 0]
cards = ["X", "J", "Q", "K", "A"]

s = ''
for i in range(n):
    s += input()

for card in s:
    t = cards.index(card)
    ans[t] += t

print(ans)