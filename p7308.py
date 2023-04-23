def get_leader(score1, score2, leader):
    if score1 > score2:
        return 0
    if score2 > score1:
        return 1
    return leader


a = int(input())
a_time = set()
for i in range(a):
    a_time.add(int(input()))

b = int(input())
b_time = set()
for i in range(b):
    b_time.add(int(input()))

a_score = 0
b_score = 0

over = 0
score = 0
leader = -1
for sec in range(1,2881):
    if sec in a_time:
        a_score += 1
    elif sec in b_time:
        b_score += 1

    # calculate score at mid
    if sec == 1440:
        score = a_score + b_score

    # judge
    new_leader = get_leader(a_score, b_score, leader)
    if leader != new_leader:
        over += 1
    leader = new_leader

print(score)
print(over-1)
