x,y = [int(x) for x in input().split()]
x_final,y_final = [int(x) for x in input().split()]
fuel = int(input())
x_distance = abs(x_final-x)
y_distance = abs(y_final-y)
needed_fuel = x_distance+y_distance
if needed_fuel <= fuel and (fuel-needed_fuel)%2==0:
    print("Y")
else:
    print("N")