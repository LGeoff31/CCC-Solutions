rows = int(input())
cols = int(input())
row = [0 for i in range(rows)]
col = [0 for i in range(cols)]
def swap(lst, idx):
    if lst[idx] == 0:
        lst[idx] = 1
    else:
        lst[idx] = 0
# print(row)
for i in range(int(input())):
    choice, num = input().split()
    num = int(num)
    if choice == "R":
        swap(row, num-1)
    else:
        swap(col,num-1)

total = 0
for char in row:
    if char == 1: total += cols
for char in col:
    if char == 1: total += rows
num_ones_in_rows = row.count(1)
num_ones_in_cols = col.count(1)

print(total-num_ones_in_rows*num_ones_in_cols*2)