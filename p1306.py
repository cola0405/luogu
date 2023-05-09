# 矩阵加速求Fib

n,m = map(int, input().split())

# 矩阵相乘
def mul(a, b):
    res = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):  # a多少行，res就多少行
        for j in range(len(b[0])):  # b多少列，res就多少列
            s = 0
            for k in range(len(b)):  # b多少列就加多少次
                s += a[i][k]*b[k][j]
            res[i][j] = s % int(1e8)
    return res

# 矩阵快速幂
def fastPow(a, b):
    res = [item for item in a]
    while b:
        if b&1:
            res = mul(res, a)
        a = mul(a, a)
        b >>= 1
    return res


def get_fib(i):
    if i <= 2:
        return 1
    res = mul(fastPow([[0,1], [1,1]], i-3), [[1],[1]])
    return res[1][0]

# 辗转相除法求最大公约数
def gcd(x, y):
    while y > 0:
        temp = x
        x = y
        y = temp%y
    return x

print(get_fib(gcd(max(n,m), min(n,m))))