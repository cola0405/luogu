s = input()
t = input()

j = 0
i = 0
while i < len(s)-1 and j < len(t):
    if s[i] == t[j]:
        j += 1
    i += 1

print(j)