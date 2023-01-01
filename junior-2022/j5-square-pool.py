n = int(input())

def get_key_by_coord(x, y):
    return f"{x}:{y}"

trees = {}
num_trees = int(input())
for i in range(num_trees):
    x, y = input().split()
    trees[get_key_by_coord(int(x) - 1,int(y) - 1)] = True

def get_ring_coordinates(row, col, sidelength):
    ring_cells = []

    for i in range(sidelength):
        ring_cells.append([row+i, col+sidelength-1])
    
    for i in range(sidelength):
        ring_cells.append([row+sidelength-1,col+i])

    
    return ring_cells

def valid_point(point):
    row, col = point

    if get_key_by_coord(row, col) in trees:
        return False
    
    if row < 0 or col < 0:
        return False
    
    if row >= n or col >= n:
        return False

    return True


def expand(row, col):
    sidelength = 1
    while True:
        ring_points = get_ring_coordinates(row, col, sidelength)

        # Check if all these are valid to expand to.
        for point in ring_points:
            if not valid_point(point):
                return sidelength - 1
        
        sidelength += 1


maximum = -99999999
for row in range(n):
    for col in range(n):
        max_sidelength = expand(row, col)
        maximum = max(max_sidelength, maximum)

print(maximum)










# n = int(input())

# def get_key_by_coord(x, y):
#     return f"{x}:{y}"

# trees = {}
# num_trees = int(input())
# for i in range(num_trees):
#     x, y = input().split()
#     trees[get_key_by_coord(int(x) - 1,int(y) - 1)] = True

# def get_ring_coordinates(row, col, rings):
#     ring_cells = []

#     # Top.
#     top_row = row - rings
#     top_start_col = col - rings
#     top_end_col = col + rings
#     for top_col in range(top_start_col, top_end_col + 1):
#         ring_cells.append([top_row, top_col])
    
#     # Bottom.
#     bottom_row = row + rings
#     bottom_start_col = col - rings
#     bottom_end_col = col + rings
#     for bottom_col in range(bottom_start_col, bottom_end_col + 1):
#         ring_cells.append([bottom_row, bottom_col])

#     # Left.
#     left_col = col - rings
#     left_start_row = row - rings
#     left_end_row = row + rings
#     for left_row in range(left_start_row, left_end_row + 1):
#         ring_cells.append([left_row, left_col])
    
#     # Right.
#     right_col = col + rings
#     right_start_row = row - rings
#     right_end_row = row + rings
#     for right_row in range(right_start_row, right_end_row + 1):
#         ring_cells.append([right_row, right_col])
#     return ring_cells

# def valid_point(point):
#     row, col = point

#     if get_key_by_coord(row, col) in trees:
#         return False
    
#     if row < 0 or col < 0:
#         return False
    
#     if row >= n or col >= n:
#         return False

#     return True


# def expand_from_centre(row, col):
#     rings = 0
#     while True:
#         ring_points = get_ring_coordinates(row, col, rings)

#         # Check if all these are valid to expand to.
#         for point in ring_points:
#             if not valid_point(point):
#                 return rings - 1
        
#         rings += 1
        
# def get_ring_coordinates_even(row, col, ring):
#     tl_row = row - ring
#     tl_col = col - ring

#     tr_row = row - ring
#     tr_col = col + ring + 1

#     bl_row = row + ring + 1
#     bl_col = col - ring

#     br_row = row + ring + 1
#     br_col = col + ring + 1

#     ring_cells = []

#     # Top.
#     for top_col in range(tl_col, tr_col + 1):
#         ring_cells.append([tl_row, top_col])
    
#     # Bottom.
#     for bottom_col in range(bl_col, br_col + 1):
#         ring_cells.append([br_row, bottom_col])
    
#     # Left.
#     for left_row in range(tl_row, bl_row + 1):
#         ring_cells.append([left_row, tl_col])

#     # Right.
#     for right_row in range(tr_row, br_row + 1):
#         ring_cells.append([right_row, tr_col])
    
#     return ring_cells


# def expand_from_centre_even(row, col):
#     rings = 0
#     while True:
#         ring_points = get_ring_coordinates_even(row, col, rings)

#         # Check if all these are valid to expand to.
#         for point in ring_points:
#             if not valid_point(point):
#                 return rings - 1
        
#         rings += 1




# max_odd = -99999999
# for row in range(n):
#     for col in range(n):
#         max_rings = expand_from_centre(row, col)
#         max_sidelength = 2 * max_rings + 1
#         max_odd = max(max_sidelength, max_odd)

# max_even = -999999999
# for row in range(n - 1):
#     for col in range(n - 1):
#         max_rings = expand_from_centre_even(row, col)
#         max_sidelength = 2 * max_rings + 2
#         max_even = max(max_sidelength, max_even)

# print(max(max_odd, max_even))


























# n = int(input())

# yard = [["" for i in range(n)] for j in range(n)]
# trees = []
# result = 0
# for i in range(int(input())):
#     row, col = [int(n) for n in input().split()]
#     row -= 1
#     col -= 1
#     trees.append([row, col])
#     yard[row][col] = "1" #One denotes a tree, empty space denotes empty

# def check(start_row, start_col, size):
#     qualified = True
#     for i in range(size):
#         if start_col + size >= n or start_row + size >= n: #Overfloat out of yard
#             qualified = False
#             break
#         if yard[start_row+size-1][start_col+i] == "1":
#             qualified = False
#             break
#         if yard[start_row+i][start_col+size-1] == "1":
#             qualified = False
#             break
#     if qualified:
#         return check(start_row, start_col, size+1)
#     else:
#         return size-1

# for i in range(n):
#     for j in range(n):
#         if yard[i][j] != "1":
#             result = max(check(i,j,2), result)
# print(result)
