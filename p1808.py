num = list(input())

if num[0] == '0':
    print('0')
elif num[0] != '-':
    num.reverse()
    ans = ''.join(num).lstrip('0')
    print(ans)
else:
    num_part = num[1:]
    num_part.reverse()
    num_part = ''.join(num_part)
    ans = '-' + num_part.lstrip('0')
    print(ans)
