x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())

direction = []
if x2 >= x1:
    direction.append('E')
else:
    direction.append('W')

if y2 >= y1:
    direction.append('N')
else:
    direction.append('S')

horizonal = 0
vertical = 0
T = int(input())
for i in range(T):
    d = input()
    if d == direction[0]:
        horizonal += 1
    elif d == direction[1]:
        vertical += 1

x_gap = abs(x2-x1)
y_gap = abs(y2-y1)
if horizonal >= x_gap and vertical >= y_gap:
    print(x_gap + y_gap)
else:
    print(-1)