# 栈操作结果 -- 卡塔兰数
n = int(input())

f = [1]
for i in range(1,n+1):
    f.append(f[-1]*(4*i-2)//(i+1))

print(f[-1])