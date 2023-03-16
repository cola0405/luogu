word = input()

abandon = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

ans = ''

for letter in word:
    if letter not in abandon:
        ans += letter

print(ans)