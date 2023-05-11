n,m = map(int, input().split())
pos = list(map(int, input().split()))
gap = [pos[i+1]-pos[i] for i in range(n-1)]
gap.sort()
print(pos[-1]-pos[0] - sum(gap[-(m-1):]) + m)
