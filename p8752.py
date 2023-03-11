ans = 0
for i in range(5):
    s = input()
    if s[0] == s[-2] and int(s[-1])-int(s[1]) == 1:
        ans += 1

print(ans)