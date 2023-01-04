n = int(input())
lst = []
for i in range(n):
    inp = input().split()
    lst.append([int(char) for char in inp])
minimum = 9812748102940184124
for elem in lst:
    for char in elem:
        if char < minimum:
            minimum = char
def check_0(lst):
    if minimum == lst[0][0]:
        return True
    else:
        return False
    
def check_90(lst):
    if minimum == lst[0][-1]:
        return True
    else:
        return False

def check_180(lst):
    if minimum == lst[-1][-1]:
        return True
    else:
        return False

def check_270(lst):
    if minimum == lst[-1][0]:
        return True
    else:
        return False

def swap_90(lst):
    result_lst = []
    z = -1
    while True:
        a = []
        for char in lst:
            a.append(char[z])
        result_lst.append(a)
        if abs(z) == len(char):
            break
        z -= 1
    return result_lst



def swap_180(lst):
    result_lst = []
    z = -1
    a = []
    for i in range(1,len(lst)+1):
        a = lst[-i][::-1]
        result_lst.append(a)
    return result_lst

def swap_270(lst):
    result_lst = []
    z = 0
    while True:
        a = []
        for i in range(1,len(lst)+1):
            a.append(lst[-i][z])
        result_lst.append(a)
        if abs(z) == len(lst[0])-1:
            break
        z += 1
    return result_lst


def display_lst(lst):
    for char in lst:
        result = ''
        for i in range(len(char)):
            result += str(char[i]) + ' '
        print(result)

if check_0(lst):
    display_lst(lst)
elif check_90(lst):
    result_lst = swap_90(lst)
    display_lst(result_lst)
elif check_180(lst):
    result_lst = swap_180(lst)
    display_lst(result_lst)
else:
    result_lst = swap_270(lst)
    display_lst(result_lst)