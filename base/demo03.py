# 引入日历模块
import calendar

import sys

# 打印我的工作日历

workDay = 0
restDay = 0

weeks = calendar.monthcalendar(2020, 6)
for week in weeks:
    for i in range(len(week)):
        day = week[i]
        if day == 0:
            week[i] = '| - '
        elif (i == 5 or i == 6):
            week[i] = '| ' + str(day) + ' <font color=Red>休息</font> '
            restDay = restDay+1
        else:
            week[i] = '| ' + str(day) + ' <font color=SeaGreen>工作</font> '
            workDay = workDay+1
        #print()
        sys.stdout.write(week[i])
    print()
#print(weeks)
print()
print('- <font color=SeaGreen>工作：'+str(workDay)+'</font>')
print('- <font color=Red>休息：'+str(restDay)+'</font>')
print('- <font color=#CC33CC>加班：0</font>')
print('- <font color=DeepSkyBlue>出差：0</font>')
print('- <font color=IndianRed>年假：0</font>')