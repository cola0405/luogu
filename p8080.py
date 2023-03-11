n = int(input())
seat = input()

ans = n+1
i = 0
while i+1<n:
    if seat[i] == 'L' and seat[i+1] == 'L':
        ans -= 1
        i += 1
    i += 1

print(min(n, ans))
