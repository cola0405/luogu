n = int(input())

ans = 0
cards = ["X", "J", "Q", "K", "A"]

s = ''
for i in range(n):
    s += input().strip()

for card in s:
    if card in cards:
        score = cards.index(card)
        ans += score

print(ans)