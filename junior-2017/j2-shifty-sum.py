a = int(input())
b = int(input())

total = a
for i in range(b):
    total += a*10
    a*=10
print(total)