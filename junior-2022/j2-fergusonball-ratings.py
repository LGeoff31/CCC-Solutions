lst = []
for i in range(int(input())):
    a = int(input())
    b = int(input())
    lst.append(a*5-b*3)

result = 0
for elem in lst:
    if elem > 40:
        result += 1

if result == len(lst):
    print(f"{result}+")
else: print(f"{result}")
