s = input()
ans = len(s)
space_num = s.count(' ')
n_num = s.count('\n')

ans -= space_num + n_num
print(ans)