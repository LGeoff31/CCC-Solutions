lst = []
for i in range(int(input())):
    name = input()
    bet = int(input())
    lst.append([name, bet])

def find_max_bet():
    max_value = -10e9
    for key, value in lst:
        if value > max_value:
            max_value = value
    return max_value
for char in lst:
    if find_max_bet() in char:
        print(char[0])
        break



