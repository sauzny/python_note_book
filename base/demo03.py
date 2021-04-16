# 引入日历模块
import calendar

import sys

# 打印我的工作日历

workDay = 0
restDay = 0
month = 5
weeks = calendar.monthcalendar(2021, month)

jobDays = [[] for i in range(6)]
jobDaysIndex = 0

print('# ' + str(month) + '月日报')
print()
print('## 一、日历')
print()
print('| 星期一 | 星期二 | 星期三 | 星期四 | 星期五 | <font color=red>星期六</font> | <font color=red>星期日</font> | 项目统计 |')
print('|---|---|---|---|---|---|---|---|')

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
    sys.stdout.write(' |')
    print()
#print(weeks)

print()
print('## 二、月度统计')
print()
print('| 工时统计 <br/> 实际 / 法定 | 类别统计（天） | 项目统计（天）|')
print('|---|---|---|')
print('| 出勤天数 <br/> 0 / '+str(workDay)+' | <font color=SeaGreen>工作：0</font>     | |')
print('| 平均工时 <br/> 0 / 8  | <font color=Red>休息：0</font>          | |')
print('| 总工时 <br/> 0 / '+str(workDay*8)+'  | <font color=#CC33CC>加班：0</font>      | |')
print('|                       | <font color=DeepSkyBlue>出差：0</font>  | |')
print('| 使用年假 <br/> 0 小时 | <font color=IndianRed>年假：0</font>    | |')
print('| 使用倒休 <br/> 0 小时 | <font color=#DF0101>倒休：0</font>      | |')
print('| 获得倒休 <br/> 0 小时 |                                         | |')

print()
print('## 三、详情')

for jobDay in jobDays:
    if len(jobDay) > 0:
        print()
        print('### ' + str(jobDay))
        print()
        for day in jobDay:
            print('- ' + str(day) + "：XXX")
            print('  - XXX')
