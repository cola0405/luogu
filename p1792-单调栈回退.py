# 有时优先选最大值可能达不到全局最优

"""
4 2
4 7 8 6
"""
import heapq

n,m = map(int, input().split())
A = list(map(int, input().split()))
heapA = [(-A[i], i) for i in range(n)]

# build for exact "next" and "pre"
# for example:
# "1 2 3 4 5 6 7"
# plant a tree at 7
# then the pre of 7 is 5, the next of 5 is 7
# so 7 is the exact next of 5
nxt = [(i+1)%n for i in range(n)]
pre = [i-1 for i in range(n)]

# make minus for max heap
heapq.heapify(heapA)

vis = [0]*n
def get_top():
    while len(A) > 0:
        top_val, top_idx = heapq.heappop(heapA)
        if vis[top_idx] == 0:
            return top_val, top_idx

def del_item(i):
    nxt[pre[i]] = nxt[i]
    pre[nxt[i]] = pre[i]
    vis[i] = 1

def main():
    ans = 0
    if m > n//2:
        print('Error!')
        return

    for i in range(m):
        top_val, top_idx = get_top()
        ans += top_val*-1

        # !!! update the value to avoid overlap
        # "1 2 3 4 5 6 7"
        # "7"已计入ans，留下剩余价值才不会overlap
        A[top_idx] = A[pre[top_idx]] + A[nxt[top_idx]] - top_val*-1
        heapq.heappush(heapA, (A[top_idx]*-1, top_idx))

        # remove pre and nxt
        # recursive delete
        del_item(pre[top_idx])
        del_item(nxt[top_idx])

    print(ans)

main()




