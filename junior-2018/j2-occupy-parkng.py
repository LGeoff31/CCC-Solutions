a = int(input())
b = input()
c = input()
total = 0
for i in range(len(b)):
    if b[i] == c[i] and b[i] == ".":
        total += 1
print(total)