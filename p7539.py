m = list(map(int, input().split()))

ac_flag = 0
de_flag = 0
for i in range(len(m)-1):
    if m[i+1] > m[i]:
        ac_flag = 1
    elif m[i+1] < m[i]:
        de_flag = 1

if ac_flag and de_flag:
    print("mixed")
elif ac_flag == 1:
    print("ascending")
else:
    print("descending")