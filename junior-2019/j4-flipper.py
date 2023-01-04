lst = [[1,2], [3,4]]
def horz_flip():
    lst[0][0], lst[1][0] = lst[1][0], lst[0][0]
    lst[0][1], lst[1][1] = lst[1][1], lst[0][1]
def vert_flip():
    lst[0][0], lst[0][1] = lst[0][1], lst[0][0]
    lst[1][0], lst[1][1] = lst[1][1], lst[1][0]
for char in input():
    if char == "H":
        horz_flip()
    else:
        vert_flip()
print(lst[0][0], lst[0][1])
print(lst[1][0], lst[1][1])
