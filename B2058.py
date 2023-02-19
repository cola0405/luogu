n = int(input())

bronze = 0
silver = 0
gold = 0

for i in range(n):
    a,b,c = map(int, input().split())
    bronze += a
    silver += b
    gold += c

total = bronze + silver + gold
print(bronze, silver, gold, total)