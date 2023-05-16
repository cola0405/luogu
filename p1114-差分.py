# 以男女差值做y值，画曲线图
# 区间男女数量相等，也就是画平行于x轴的直线与曲线相交，U型
# 换句话说，i点和j点差值相等的，则说明区间[i,j]男女数量相等
# 则题目是要求差值相等（不一定是差值为0）的最大跨度
n = int(input())
p = input().split()

max_len = 0
d = {0: 0}
idx = 1

diff = 0
for people in p:
    if people == '0':
        diff += 1
    else:
        diff -= 1
    if diff not in d:
        d[diff] = idx
    else:  # 如果这个diff是之前出现过的，则拿当前长度尝试更新max_len
        max_len = max(idx-d[diff], max_len)
    idx += 1

print(max_len)

"""
4
1 1 0 0
"""