
lst_x=[]
lst_y=[]
for i in range(int(input())):
    x,y = input().split(",")
    lst_x.append(int(x))
    lst_y.append(int(y))
print(f"{min(lst_x)-1},{min(lst_y)-1}")
print(f"{max(lst_x)+1},{max(lst_y)+1}")


