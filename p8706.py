s = input()

ans = ''
for i in range(len(s)):
    if '1' <= s[i] <= '9':
        ans += s[i-1] * (int(s[i])-1)
    else:
        ans += s[i]

print(ans)
