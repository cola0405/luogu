s = list(input())
n = int(input())

t = s.copy()
t.sort()
t = t[:len(s)-n]


for num in t:
    num_inx = s.index(num)
    if num_inx < n:
        continue
    


i = 0
ans = []
while i<len(s):
    if s[i] in t:
        ans.append(s[i])
        s.remove(s[i])
    i+=1

print(''.join(ans))


