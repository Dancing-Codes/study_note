import random

# 总计239行代码，预计阅读时长15min
# 1、比较（关系）运算符
"""
 运算符     描述      示例
 >      大于，则真   a=4,b=3 则 (a>b) 为真
 <      小于，则真   a=3,b=4 则 (a<b) 为真
 ==     等于，则真   a=3,b=3 则 (a==b) 为真
 >=     大于等于，真
 <=     小于等于，真
 !=     不等于，真
"""
# 示例代码
a = 3
b = 4
print(a > b)

# 2、逻辑运算符
"""
and  与
or   或
not  非
"""
# 代码示例
print((1 > 0) and (0 > 1))
print(not (1 == 1))
# 短路运算
0 and print("输出内容1")  # 当遇到0为false时，不再向下执行
1 or print("输出内容2")  # 当遇到1为true时，不再向下执行

# 3、if语句基本格式
"""
if 要判断的条件: 条件为true时才执行下面代码
    条件满足时，要做的事情
    ……
else:
    ...条件不满足时要做的事情
"""
# 注意，一个tab键后的代码都是if的语句块，保持代码对齐
sex = 'man'
if sex == 'man':
    print("是个男孩")
else:
    print("女孩")

# 4、if实现三目运算符
a = 3
b = 4
maxNum = a if a > b else b

# 5、if...elif...else的使用
if sex == 'man':
    print("是个男孩")
elif sex == 'woman':
    print("是个女孩")
else:
    print("不确定")

# 6、if语句嵌套
"""
if 条件 1:
    条件 1 满足执行的代码
    ……

    if 条件 1 基础上的条件 2:
        条件 2 满足时，执行的代码
        ……

    # 条件 2 不满足的处理
    else:
        条件 2 不满足时，执行的代码

# 条件 1 不满足的处理
else:
    条件1 不满足时，执行的代码
"""
# 代码示例
food = 'fruit'
fruit = 'apple'
if food == 'fruit':
    print("食物是水果")
    if fruit == 'apple':
        print("水果是苹果")
    elif fruit == 'banana':
        print("水果是香蕉")
    else:
        print("不知道水果是什么")
else:
    print("不知道食物是什么")

# 猜拳游戏
"""
1 石头
2 剪刀
3 布
"""
userNum = int(input("输入你的数字："))
computerNum = random.randint(1, 3)
if (userNum == 1 and computerNum == 2) or (userNum == 2 and computerNum == 3) or (userNum == 3 and computerNum == 1):
    print("你赢了")
elif userNum == computerNum:
    print('打了个平手')
else:
    print('再接再厉')

# 7、循环语句while
"""
while true: #死循环
    ...
    #break 跳出循环
    #continue 开始下一次循环
"""
# 代码示例
i = 1
sumI = 0
while i <= 100:
    i += 1
    sumI += i
print(sumI)
# 循环嵌套
i = 1
while i <= 5:
    print("跑完第%d圈" % i)
    j = 1
    while j <= 10:
        print("做完第%d个俯卧撑" % j)
        j += 1
    i += 1
# 打印星星
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*', end='')
        j += 1
    print()
    i += 1
# 打印三角形
i = 0
while i < 5:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("*", end='')
    print()
## 进阶：杨辉三角 ##
"""
                                        1                               n = 1
                                    1       1                           n = 2
                                1       2       1                       n = 3
                            1       3       3       1                   n = 4
                        1       4       6       4       1               n = 5
                    1       5       10      10      5       1           n = 6
                1       6       15      20      15      6       1       n = 7
            1       7       21      35      35      21      7       1   n = 8
"""

# while/for循环的else
# 当while里面没有遇到break时，while循环执行完后会执行else语句
i = 0
print("循环前")
while i < 2:
    i += 1
    print("循环里")
else:
    print("else 里")
"""
if...else...语句和while...else... 语句的区别
if...else:当满足条件时，执行if内的语句，否则执行else内的语句
while...else:当满足循环条件时，循环，循环执行完后在循环语句块里没有碰到break语句时，执行else语句块里的内容
"""

# 世界杯案例
# method 1
myTeam = int(input("输入我们球队的实力值："))
myScore = 0
otherTeam1 = int(input("输入球队1的实力值："))
otherTeam2 = int(input("输入球队2的实力值："))
otherTeam3 = int(input("输入球队3的实力值："))
otherTeam4 = int(input("输入球队4的实力值："))
print("小组赛第一场")
if myTeam > otherTeam1:
    myScore += 3
    print('我方胜')
elif myTeam == otherTeam1:
    myScore += 1
    print('平局')
else:
    myScore += 0
    print('我方败')

print("小组赛第二场")
if myTeam > otherTeam2:
    myScore += 3
    print('我方胜')
elif myTeam == otherTeam2:
    myScore += 1
    print('平局')
else:
    myScore += 0
    print('我方败')

print("小组赛第三场")
if myTeam > otherTeam3:
    myScore += 3
    print('我方胜')
elif myTeam == otherTeam3:
    myScore += 1
    print('平局')
else:
    myScore += 0
    print('我方败')

print("小组赛第四场")
if myTeam > otherTeam4:
    myScore += 3
    print('我方胜')
elif myTeam == otherTeam4:
    myScore += 1
    print('平局')
else:
    myScore += 0
    print('我方败')

print("我们球队最终得分：%d" % myScore)

# method 2 三行代码
list_team = [myTeam, otherTeam1, otherTeam2, otherTeam3, otherTeam4]
list_team.sort()
print("我们球队的最终得分：%d" % (list_team.index(myTeam) * 3 + (list_team.count(myTeam) - 1)))

