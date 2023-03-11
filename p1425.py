a,b,c,d = map(int, input().split())

def get_time_gap(h1,m1,h2,m2):
    hour = h2 - h1
    if m2 < m1:
        hour -= 1
        print(hour, d+60-b)
    else:
        print(hour, d-b)

get_time_gap(a,b,c,d)


