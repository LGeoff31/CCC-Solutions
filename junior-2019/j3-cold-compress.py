for j in range(int(input())):
    a = input()
    a += "]"
    result = ""
    num = 1
    for i in range(len(a)-1): #make seperate case if last number isnt same
        if a[i] != a[i+1]:
            result += str(num) + " " + a[i] + " "
            num = 1
        else:
            num += 1
    print(result)
