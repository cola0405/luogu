s = input()

res = ''
i = 0
while i<len(s):
    if i+1 < len(s) and '1' <= s[i+1] <= '9':
        repeating_sequence = s[i]*int(s[i+1])
        res += repeating_sequence
        i += 1
    elif i+1 <= len(s):
        res += s[i]
    else:
        break
    i += 1
print(res)