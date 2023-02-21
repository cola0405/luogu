# 原地下降数


num = list(input())
k = int(input())

remain_num = len(num) - k
del_num = 0
i = 0
while i+1 < len(num) and del_num < k:
    if num[i] > num[i+1]:
        del_num += 1
        num.pop(i)

        # 得确保前面的数字是尽可能小的，不能过了就过了
        if i > 0:
            i -= 1
    elif num[0] == '0':
        num.pop(0)
    else:
        i += 1

# 在有序的基础上，后面多的尾巴肯定是直接删去的
print(''.join(num[:remain_num]))



# 50074897
# 2
# 4897


# 247062143405644330475617639991478539124236
# 30
# 113124236