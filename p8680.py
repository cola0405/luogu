n = int(input())

target = ['2','0','1','9']
ans = 0
for num in range(1,n+1):
    num = str(num)
    for digit in target:
        if digit in num:
            ans += int(num)
            break

print(ans)

