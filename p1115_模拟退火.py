# 1217778
# -100

n = int(input())
nums = list(map(int, input().split()))

import math
import random

def get_sum(l, r):
    return sum(nums[l:r+1])

l,r = 0, n-1
T = 100000
# alpha = 0.999999 得到了！！！！ -100
alpha = 0.999999
stopping_T = 1e-8
stopping_iter = 50000000

best_l, best_r = 0, n-1
max_val = get_sum(l, r)
val = max_val
delta = 0
i = 0
while T > stopping_T and i < stopping_iter:
    l += random.randint(-1,1)
    r += random.randint(-1,1)
    l = max(l, 0)
    l = min(l, n-1)
    r = max(l, r)
    new_val = get_sum(l, r)
    delta = new_val - val

    # get better val or probability fit
    if delta > 0 or math.exp(delta / T) > random.random():
        val = new_val
        print(max_val, val, l, r)
        if new_val > max_val:
            max_val = new_val
            best_l, best_r = l, r
    i += 1
    T *= alpha

print(max_val)