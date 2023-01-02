target = int(input())
infected = int(input())
a = infected
r = int(input())
days = 0

while infected <= target:
    days += 1
    infected += a*(r**days)
print(days)