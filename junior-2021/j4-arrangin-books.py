books = input()
swaps = 0

l_count = books.count("L")
m_count = books.count("M")
s_count = books.count("S")

not_correct_in_L=0
not_correct_in_M=0
MinL = 0
LinM = 0

for char in books[:l_count]:
    if char != "L":
        not_correct_in_L += 1
    if char == "M": MinL+=1

for char in books[l_count:m_count+l_count]:
    if char != "M":
        not_correct_in_M += 1
    if char == "L":
        LinM+=1
# print(not_correct_in_L)
# print(not_correct_in_M)

print(not_correct_in_L+not_correct_in_M-min(MinL,LinM))
# print(books[:l_count])
# print(books[l_count:m_count+l_count])