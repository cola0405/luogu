# 找规律
# 当甲赢时，肯定是甲比乙多取了一个石子 -- k+(k+1) = 2k+1
# 当乙赢时，肯定时甲和乙取的石子刚刚好 -- k+k = 2k

n = int(input())

stone = sum(map(int, input().split()))

if stone % 2 == 0:
    print('Bob')
else:
    print('Alice')