import collections
import sys
rows = int(sys.stdin.readline())
cols = int(sys.stdin.readline())
board = []

for i in range(rows):
    a = [int(x) for x in sys.stdin.readline().split()]
    board.append(a)
queue = collections.deque([(1,1)])
searched = collections.deque([(1,1)])

def get_next(loc):
    lst = []
    x,y = loc
    num = board[x-1][y-1]
    for i in range(1,num+1):
        if num%i==0: #Check factors
            if i<=rows and num//i <= cols: #Check within board
                lst.append([i, num//i])
    return lst

steps = 0
p = 1
while len(queue) > 0:
    if [rows, cols] in queue:
        p=0
        break

    for i in range(len(queue)):
        loc = queue.popleft()
        for new_loc in get_next(loc):
            if new_loc not in searched:
                queue.append(new_loc)
                searched.append(new_loc)

if p==0: 
    print("yes")
else: 
    print("no")