a = int(input())
b = int(input())
c = int(input())
d = int(input())
qualfied = False
if a == 8 or a == 9:
    if d == 8 or d == 9:
        if b == c:
            qualfied = True
if qualfied: print("ignore")
else: print("answer")