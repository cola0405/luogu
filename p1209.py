m,s,c = map(int, input().split())

cows = []
for i in range(c):
    cows.append(int(input()))

cows.sort()
gaps = []
for i in range(c-1):
    gaps.append(cows[i+1] - cows[i])

ans = cows[-1] - cows[0]
count = 1
for i in range(m-1):
    if len(gaps) == 0:
        break
    # 贪心，每次消最大的gap
    max_gap = max(gaps)
    ans -= max_gap
    gaps.remove(max_gap)
    count+=1

ans += count
print(ans)
