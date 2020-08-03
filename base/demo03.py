# 引入日历模块
import calendar

import sys

# 打印我的工作日历

workDay = 0
restDay = 0
month = 8
weeks = calendar.monthcalendar(2020, month)

jobDays = [[] for i in range(6)]
jobDaysIndex = 0

print('# ' + str(month) + '月日报')
print()

print('星期一 | 星期二 | 星期三 | 星期四 | 星期五 | <font color=red>星期六</font> | <font color=red>星期日</font>')
print('---|---|---|---|---|---|---')

for week in weeks:
    for i in range(len(week)):
        day = week[i]
        if day == 0:
            week[i] = '| - '
        elif (i == 5 or i == 6):
            week[i] = '| ' + str(day) + ' <font color=Red>休息</font> '
            restDay = restDay+1
            if i == 5 :
                jobDaysIndex = jobDaysIndex + 1
        else:
            week[i] = '| ' + str(day) + ' <font color=SeaGreen>工作</font> '
            workDay = workDay+1
            jobDays[jobDaysIndex].append(day)
        #print()
        sys.stdout.write(week[i])
    print()
#print(weeks)

print()

print('日历统计（天）：')
print()
print('<font color=SeaGreen>工作</font> | <font color=Red>休息</font> | <font color=#CC33CC>加班</font> | <font color=DeepSkyBlue>出差</font> | <font color=IndianRed>年假</font> | <font color=#DF0101>倒休</font>')
print('-------|--------|--------|------|------|------')
print('<font color=SeaGreen>'+str(workDay)+'</font> | <font color=Red>'+str(restDay)+'</font> | <font color=#CC33CC>0</font> | <font color=DeepSkyBlue>0</font> | <font color=IndianRed>0</font> | <font color=#DF0101>0</font>')

print()
print('工时统计：')
print()
print('items | 实际 | 法定要求')
print('-------|--------|------')
print('出勤天数 | 0 | '+str(workDay))
print('平均工时 | 0 | 8')
print('总工时 | 0 | '+str(workDay*8))
print('使用倒休小时 | 0 | -')
print('获得倒休小时 | 0 | -')

print()
print('工作日汇总统计（天）：')
print()
print('星期\\项目 | XXX | XXX | XXX | 汇总')
print('-------|--------|--------|------|------')
for jobDay in jobDays:
    if len(jobDay) > 0:
        print(str(jobDay) + ' | 0 | 0 | 0 | 0')
print('汇总    | 0  | 0 | 0   | 0')

print()
print('详情：')

for jobDay in jobDays:
    if len(jobDay) > 0:
        print()
        print('## ' + str(jobDay))
        print()
        for day in jobDay:
            print('- ' + str(day) + "：XXX")
            print('  - XXX')
