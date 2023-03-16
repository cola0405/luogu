n = int(input())
seat = input()

ans = n+1 - seat.count("L")//2
print(min(n, ans))

