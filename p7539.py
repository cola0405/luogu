m = list(map(int, input().split()))

ac = 0
de = 0
for i in range(len(m)-1):
    if m[i+1] > m[i]:
        ac = 1
    elif m[i+1] < m[i]:
        de = 1

if ac and de:
    print("mixed")
elif ac == 1:
    print("ascending")
else:
    print("descending")

