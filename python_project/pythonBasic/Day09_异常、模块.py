#异常介绍
#当程序运行时，python解释器遇到了一个错误，这时解释器无法继续运行了，出现了一次错误的提示，这就是异常
#异常不是语法错误，而是程序运行时出错了，比如前面的递归深度超过996的函数，解释器抛出超出最大深度的错误
#常见的内置异常
# FileNotFoundError
# UnsupportedOperation
# TypeError
# ZeroDivisionError
# import threading
import sys
#异常处理
#解释器遇到异常时，默认执行的动作是终止程序
#处理异常的目的：防止异常程序退出，保证程序正常执行
# try:...except:... 如果try里的代码块发生异常，自动跳转到except中
try:
    print(1/0)
except:
    print(f'print函数里发生了除零异常')

#捕获指定异常
"""
try:
    可能异常的代码块
except 异常类型:
    处理异常的代码块
"""
try:
    file = open('xxxx.txt', 'r')
except FileNotFoundError:
    print(f'try里发生了文件未找到异常')

#捕获多个异常
try:
    print(1/0)
    open('xxx.txt', 'r')
except (FileNotFoundError, ZeroDivisionError):
    print('try里发生了除零异常和文件未找到异常')
#获取异常的信息描述
try:
    open('xxx.txt', 'r')
except FileNotFoundError as e:
    print('异常信息为:', e)

#捕获任意类型的异常
"""
try:
    可能的异常代码
except Exception as e:
    处理代码
"""  #Exception是所有异常类型的父类

# 异常中的else
# 在if中，它的作用是当条件满足时执行的
# 同样try:...except:...也是，如果没有捕获到异常，就执行else，另外for和while循环里没有遇到break时也可以加else
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s' % errorMsg)
else:
    print('没有捕获到异常，真高兴')

#try:...finally:
"""
try:
    可能发生的异常
except:
    处理的代码
else:
    不发生异常时执行
finally:
    不管有没有异常，都要执行
"""

#异常传递
#传递特点，当异常发生时，当前代码块没有捕获处理，这个异常就会向上传递
#异常嵌套
#函数嵌套时，异常也会向外层函数传递

#自定义异常抛出和接收，继承Exception异常基类
class MyException(Exception):
    def __init__(self):
        super(MyException, self).__init__()
    #重新定义异常输出信息
    def __str__(self):
        return 'my code error'

try:
    #抛出一个我自己定义的异常
    raise MyException()
except MyException as me:
    print('异常信息为：', me)


#模块
#1、模块是一个有python代码块组成的文件，就是一个以.py结尾的文件
#2、模块包含函数、类和变量，还可以包括可运行的代码，类似C++的库和Java的包
#3、模块的作用：
#  3.1、提高代码的复用性和可维护性----许多库和包的共同特点
#  3.2、避免名字冲突
#  3.3、提前封装好执行相应功能的代码块，提高程序执行效率
#导入模块
"""
导入格式：import 模块名  例如：import math
使用格式：模块名.函数  模块名.类名  模块名.变量名
"""
#from.. module name。.import...导入模块中需要的内容
# 这个声明不会把整个模块导入到当前的命名空间中，它只会将里的函数引入进来
# 这种导入的方法不会把被导入的模块的名称放在当前的字符表中
"""
导入格式： from 模块名 import 需要使用的函数、类、变量
使用格式： 函数、类、变量，无需通过模块引用
"""
#from...import * 导入模块全部内容
#import...as..给导入的模块取别名
"""
把复杂名字改简单些
把已经同名的名字改一个不同名的名字
"""

#模块搜索路径：
# 1、当前目录
# 2、如果不存在当前目录，python则搜索系统路径
# 3、模块搜索路径存储在sys.path中（环境变量）
"""
import sys
sys.path    查看搜索路径
sys.path输出的是一个列表，第一项是空串，代表当前路径
在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。
import并没有把sys里的函数名称写入到当前符号表里，只是把sys模块的名字写到了那里，通过模块来访问函数
"""

# 制作一个模块
# 深入模块
"""
模块除了方法定义，还包括可执行的代码，这些代码在第一次被导入时才会执行
    每个模块都有独立的符号表，在模块内部所有的函数当作全局符号表来使用
    所以，模块的作者可以大胆放心的在模块内部使用这些全局变量，而不用担心和其他变量搞混
    从另一个方面，当你确实知道你在做什么的话，你也可以通过 modname.itemname 这样的表示法来访问模块内的函数。
模块是可以导入其他模块的。在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，当然这只是一个惯例，而不是强制的。被导入的模块的名称将被放入当前操作的模块的符号表中。
"""

#给模块取别名
# import random as ri
# num = ri.randint(1, 3)
#给模块的函数取别名
# from random import randint as ri
# ri(1, 3)

#模块搜索路径
print(sys.path)
# path 是个列表，追加解释器的寻找路径
# sys.path.append('path')
"""
路劲优先级自上而下，保证自己的模块名不要和系统的模块重名，否则会遮挡系统模块名
[ 'D:\\python_project\\python基础',
  'D:\\python_project',
  'C:\\Users\\wuyupeng\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 
  'C:\\Users\\wuyupeng\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 
  'C:\\Users\\wuyupeng\\AppData\\Local\\Programs\\Python\\Python38\\lib', 
  'C:\\Users\\wuyupeng\\AppData\\Local\\Programs\\Python\\Python38', 
  'C:\\Users\\wuyupeng\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
"""
#module.py，每个python文件都可以当作一个模块
#模块的名字就是文件的名字
#import module #导入自己的模块
#模块中的__name__属性
"""
个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
"""
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自其他模块')
"""
每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
"""
#python的内置函数dir()
#dir(module_name)  可以找到模块内所有定义的名称，以字符串列表的形式返回

#模块中的__all__
"""
模块中的__all__变量，只对 from module_name import * 这种导入方式有效
__all__变量包含的元素才会被  from ... import * 导入
格式：
__all__ = ['变量名'， '类名'， '函数名']
"""

#制作一个模块
"""
制作自定义模块
把写好的代码放在一个py文件中，这个py文件就是模块文件，后续方便别人导入使用
模块中__name__的作用
直接运行此文件，__name__的结果为__main__
此文件被当做模块文件导入时，__name__的结果不为__main__
如果不想导包把模块的测试代码也运行，把模块的测试代码放在if __name__ == '__main__':条件语句里面
使用from...import*时__all__在模块中的作用
模块中__all__变量，只对from xxx import *这种导入方式有效
模块中__all__变量包含的元素，才能会被from xxx import *导入
"""