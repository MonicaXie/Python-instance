# 任务：输入某年某月某日，判断这一天是这一年的第几天？

# 方法一

year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
sum = 0
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] 
if 1 <= month <= 12:
    sum = months[month - 1]
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day.' % sum)
else:
    print('data error')

# 方法二

def day_num(): 
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: '))
    if not 1 <= month <= 12:
        return 'data error'
    sum = day
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) :
        months[1] = 29
    for i in range(month - 1):
        sum += months[i]
    return 'it is the %dth day.' % sum
print(day_num())
