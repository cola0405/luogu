# 以男女差值做y值，画曲线图
# 区间男女数量相等，也就是画平行于x轴的直线与曲线相交，U型
# 换句话说，i点和j点差值相等的，则说明区间[i,j]男女数量相等
# 则题目是要求差值相等（不一定是差值为0）的最大跨度


n = int(input())
query = input().split()

# key-value: 差值-最大跨度
# ps:这里的初始化要注意，不是初始化为0
# 因为第一个diff为0是在第一位之前-1的位置
# 之后求区间长度时才不会出错
d = {0: [-1,-1]}
ans = 0
diff = 0
for i in range(n):
    if query[i] == '0':
        diff += 1
    else:
        diff -= 1

    if diff in d:
        d[diff][0] = min(i, d[diff][0])
        d[diff][1] = max(i, d[diff][1])
        if d[diff][1]-d[diff][0] > ans:
            ans = d[diff][1]-d[diff][0]
    else:
        d[diff] = [i,i]

print(ans)