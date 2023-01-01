must_be_together = []
dic = {}
for i in range(int(input())):
    must_be_together.append(input().split())
must_not_be_together = []
for j in range(int(input())):
    must_not_be_together.append(input().split())

violations = 0
people = []
for i in range(int(input())):
    a,b,c = input().split()
    dic[a] = [b,c]
    dic[b] = [a,c]
    dic[c] = [a,b]

def check_same_group(x,y):
    lst = dic[x]
    return y == lst[0] or y == lst[1]


for x,y in must_be_together:
    if not check_same_group(x,y):
        violations += 1

for x,y in must_not_be_together:
    if check_same_group(x,y):
        violations += 1

print(violations)
