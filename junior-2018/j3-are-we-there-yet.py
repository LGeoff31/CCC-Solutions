lst = [int(x) for x in input().split()]
for i in range(5):
    result = str(sum(lst[:i])) + " "
    result += str(sum(lst[:i]) - lst[i]) + " "
    print(result)
