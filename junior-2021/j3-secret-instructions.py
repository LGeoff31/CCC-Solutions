lst = []
while True:
    a = input()
    if a == "99999":
        break
    if (int(a[0]) + int(a[1])) == 0:
        output_string = lst[-1][0]
    elif (int(a[0]) + int(a[1])) % 2 == 0:
        output_string = "right"
    else:
        output_string = "left"
    output_num = a[2:]
    lst.append([output_string,output_num])

for char in lst:
    print(char[0], char[1])
        
        
    