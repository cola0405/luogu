s = input().split()

short_word = s[0]
long_word = s[0]

for word in s:
    if len(word) > len(long_word):
        long_word = word
    if len(word) < len(short_word):
        short_word = word

print(long_word)
print(short_word)