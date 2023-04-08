s = input()

if s[:3] == 'MDA':
    print('1 1 1 1 1')
else:
    def get_tail(s):
        i = len(s)-1
        while i>=0:
            if '0' <= s[i] <= '9':
                return s[i]
            i -= 1

    # 获得尾号
    tail = get_tail(s)

    ans = []
    limits = ['19', '28', '37', '46', '50']
    for limit in limits:
        if tail in limit:
            ans.append('1')
        else:
            ans.append('0')

    print(' '.join(ans))