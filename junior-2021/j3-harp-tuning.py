str = input()
lst = []
for i in range(len(str)-1): #O(len(str))
    if str[i].isdigit() and not str[i+1].isdigit():
        lst.append(i)
lst.append(len(str))
lst.insert(0,0) #O(len(lst))
a = []
for i in range(len(lst)-1): #O(len(lst))
    if i == 0:
        a.append(str[lst[i]:lst[i+1]+1])
    else:
        a.append(str[lst[i]+1:lst[i+1]+1])

def make_nice(string): #(O(len(string))
    if "-" in string:
        number = string[string.index("-")+1:] #O(len(string))
        string = string[:string.index("-")]  #O(len(string))
        print(f"{string[0:len(string)]} loosen {number}")
    else:
        number = string[string.index("+")+1:]
        string = string[:string.index("+")]
        print(f"{string[0:len(string)]} tighten {number}")

for elem in a: #O(len(a) * O(len(elem)))
    make_nice(elem)

"""
Time Complexity: O(n*m), n=#elements in a, m=maximum length element in a: QUADRATIC
"""
