minutes = int(input())

hour = 12
minute = 0
count = 0
cycles = minutes // 1440
minutes %= 1440
def check_time_arithmetic(hour, minute):
    hour = str(hour)
    minute = str(minute)
    if len(minute) == 1:
        minute += "0"
        minute = minute[::-1]
    if len(hour) == 1:
        diff = int(hour) - int(minute[0])
        if int(minute[0]) - int(minute[1]) == diff:
            return True
    else:
        diff = int(hour[0]) - int(hour[1])
        if int(hour[1]) - int(minute[0]) == diff == int(minute[0]) - int(minute[1]):
            return True
    return False

for i in range(minutes):
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1
        if hour == 13:
            hour = 1
    if check_time_arithmetic(hour, minute):
        count += 1

print(count+(cycles*62))

