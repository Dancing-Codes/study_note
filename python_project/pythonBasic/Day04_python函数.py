# 总计155行代码，预计阅读时间13min
# python函数
# 函数是组织好的，可重复使用的，用来实现单一的，或相关联功能的代码段
# 函数能提高应用的模块性，和代码的重复利用率。python有很多内建函数，比如print，sort
# 你也可以创建自己的函数，并且调用，这被叫做用户自定义函数

# 定义一个函数,系统建议在函数的定义上下空至少两行


def _max(a: int, b) -> int:  #求最大值函数
    if a > b:
        return a
    else:
        return b


print(_max(1, 5))


def hello():    # hello函数
    print('Hello World')


hello()


#参数传递
# 在 python 中，类型属于对象，变量是没有类型的：
val = [1, 2, 3]
val = 'Runoob'
#以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 val 是没有类型，她仅仅是一个对象的引用（一个指针），
#可以是指向 List 类型对象，也可以是指向 String 类型对象。

#可更改（mutable）和不可更改对象(immutable)
#在python中，string，tuple和numbers是不可更改对象，list和dict是可更改对象
"""
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
"""
#python 函数的参数传递,python的传参方式都是引用传递，但有些引用是可变的，有些是不可变的
"""
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
"""
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
# 传不可变对象的实例----值传递
def _change(a):
    print(id(a))    #140718077695936
    a = 1
    print(id(a))    #140718077695648    产生了一个新的对象

val = 10
print(id(val))      #140718077695936
_change(val)
print(val)          #val的值没有改变

# 传可变对象实例
def _change_list(mylist):
    mylist.append([4, 5, 6])
    print("函数内取值：", mylist)
    return
mylist1 = [1, 2, 3]
_change_list(mylist1)
print('函数外打印：', mylist1)

#参数
"""
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
"""
#必须参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
#就像_max函数，必须传入两个参数，否则会出现语法错误

#关键字参数
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#测试用例
def printer(str, list):
    print(str)
    print(list)

test_list = ['美女', '今年几岁了']
printer(str='你好啊', list=test_list)  #如果前面用了关键字参数，后面不用，则报语法错误
#测试用例
def print_info(name, age):
    print(name, age)
print_info(age=10, name='wuyupeng')     #打印wuyupeng 10

#默认参数 ----默认参数必须放在参数列表的最后
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
def print_info_default(age=10):
    print("my age is :%d" % age)

#不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数，当然，也可以不传递未命名的变量。
def class_name(arg1, *var_tuple):
    print(arg1)
    print(var_tuple)
class_name('伍宇鹏', '陈嘉铭', '董小姐')
# 还有一种就是参数带两个星号 **基本语法如下：
# 加了两个星号 ** 的参数会以字典的形式导入
def student_name(arg1, **dic_stu):
    print(arg1)
    print(dic_stu)
student_name('伍宇鹏', a='陈嘉铭', b='董小姐')  #必须给参数命名，其中参数名用作字典的key，参数值用作value，如果key重复,报语法错误
#声明函数时，*可以在参数列表中单独出现
def test_fun1(a, b, *, c):  #如果单独出现星号 * 后的参数必须用关键字传入
    return a + b + c
test_fun1(1, 2, c=3)

#匿名函数lambda表达式
sum_lambda = lambda arg1, arg2: arg1+arg2
print('10，20相加后的值', sum_lambda(10, 20))

# return语句，函数返回值，函数没有返回值，则返回none对象

# 强制位置参数
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参

# def test_func2(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)

# 参数提示
def arg_tell(name: str, age: 'int > 0' = 20):
    pass


#函数进阶----递归
#1、Fibonacci数列
#编写一个函数，传入n，输出斐波那契数列第n项
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # 1 1 2 3 5 8 13 21 34 55……
print('fibonacci数列第10项:', fibonacci(10))
#2、二叉树中序遍历

#3、列表快速排序
list_target = [34, 13, 344, 167, 89, 56, 88, 35]
def quick_sort(array, start, end):
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        while array[right] >= mid_data and left < right:
            right -= 1
        array[left] = array[right]
        while array[left] < mid_data and left < right:
            left += 1
        array[right] = array[left]
    array[left] = mid_data
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


quick_sort(list_target, 0, len(list_target) - 1)
print("排序后的列表", list_target)
