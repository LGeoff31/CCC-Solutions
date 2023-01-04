import sys
from collections import deque  
input = sys.stdin.readline
queue = deque()
big_num = int(1e6+5)
visited = [False for i in range(big_num)]
lst = [[] for i in range(big_num)]
qualified = False
n = int(input())
m = int(input())

for i in range(1,n+1):
    input_lst = [int(x) for x in input().split()]
    for j in range(1,len(input_lst)+1):
        lst[(i)*(j)].append(input_lst[j-1])
        if i == j == 1:
            visited[input_lst[j-1]] = True
            queue.append(input_lst[j-1])

while queue:
    num = queue.popleft()
    if num == m * n:
        qualified = True
    else:
        for nxt_char in lst[num]:
            if visited[nxt_char] == False:
                visited[nxt_char] = True
                queue.append(nxt_char)

if qualified: print("yes")
else: print("no")

