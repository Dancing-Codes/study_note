# import random
# import socket
# socket.socket()
import dis
import os
from datetime import datetime
import sys
import pandas as pd
#
# # # list_info = []
# # # list_info.append(input("输入名字:"))
# # # list_info.append(input("输入年龄:"))
# # # list_info.append(input("输入电话:"))
# #
# # my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
# # new_list = []
# # for val in my_list:
# #     if val.endswith('s') or val.endswith('e'):
# #         new_list.append(val)
# # print(new_list)
# #
# # product = [
# #     {"name": "电脑", "price": 7000},
# #     {"name": "鼠标", "price": 30},
# #     {"name": "usb电动小风扇", "price": 20},
# #     {"name": "遮阳伞", "price": 50},
# # ]
# # def buy_or_not(money, _product):
# #     sum_price = 0
# #     for val in _product:
# #         sum_price += val.get('price')
# #     if sum_price <= money:
# #         print('能买')
# #         return
# #     print('不能买')
# #     return
# # buy_or_not(8000, product)
# #
# # my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
# # nums = []
# # length = len(my_list)
# # i = 0
# # while i < length:
# #     if my_list[i].endswith("s") or my_list[i].endswith("e"):
# #         nums.append(my_list[i])
# #     i += 1
# # print(nums)
# # def printer(left_border_size=5, up_border_size=5):
# #     if left_border_size == 0: return
# #     printer((left_border_size-1), up_border_size)
# #     print('*\t'*up_border_size)
#
# # print案例
# # import random
# # def print_square(left_border_size=5, up_border_size=5):
# #     if left_border_size == 0: return
# #     print_square((left_border_size-1), up_border_size)
# #     print('*\t'*up_border_size)
# # def print_triangle(_border=5):
# #     i = _border - 1
# #     j = _border - i
# #     while i >= 0:
# #         print(' '*i, end='')
# #         while j:
# #             print('* ', end='')
# #             j -= 1
# #         print()
# #         i -= 1
# #         j = _border - i
# # def _menu():
# #     flag = 0
# #     while True:
# #         flag = int(input('1、打印三角形 2、打印矩形 3、退出\n'))
# #         if flag == 1:
# #             print_triangle(random.randint(2,10))
# #         elif flag == 2:
# #             print_square(random.randint(2,10), random.randint(2,10))
# #         elif flag == 3:
# #             return
# #         else:
# #             print("输入有误，重新输入")
# #             continue
# # _menu()
#
# # 字典表达式
# key_list = ['k1', 'k2', 'k3']
# key_value = ['1', '2', '3']
# dic_v = {key_list[i]: key_value[i] for i in range(len(key_list))}
# print(dic_v)
# # 集合表达式
# set_a = {random.randint(0, 100) for i in range(10)}
# print(set_a)
# #推导式只能用于可变数据类型
#
# #字符串输出对齐
# print('|'+'hello'.center(10)+'|')
# print('|'+'hello'.rjust(10)+'|')
# print('|'+'hello'.ljust(10)+'|')
#
# def char_type(str_in):
#     digit_num, char_num, sp_num, other_num = 0, 0, 0, 0
#     for x in str_in:
#         if str.isdigit(x):
#             digit_num += 1
#         elif str.isalpha(x):
#             char_num += 1
#         elif str.isspace(x):
#             sp_num += 1
#         else:
#             other_num += 1
#     return digit_num, char_num, sp_num, other_num
# # res_tuple = char_type(input('请输入任意类型字符：'))
# # print(res_tuple)
#
# def find_all_pos(arg, arr_arg) -> list:
#     list_ret = []
#     for i, value in enumerate(arr_arg):
#         if value == arg:
#             list_ret.append(i)
#     return list_ret
# print(find_all_pos(3, (1, 2, 3, 3, 5, 6, 6, 4, 3)))
#
# with open('./python.txt', 'w', encoding='GBK') as file_fd:
#     file_fd.write('人生苦短，我用python')
# with open('./python.txt', 'r') as file_fd:
#     print(file_fd.read())
#
# def writer(file_name='./out.txt') -> int:
#     str_in = input('输入字符串:')
#     file = open(file_name, 'a')
#     str_in.upper()
#     num = file.write(str_in)
#     return num
# # writer()
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f'{self.age}岁的{self.name}在吃东西')
# haskey = Dog('哈士奇', 6)
# haskey.eat()

#--------------------------------------------------------------------
#作业
# #创建A文件
# def reader(file_name='A.txt'):
#     file_fd = open(file_name, 'r')
#     str_read = file_fd.read()
#     list_str = str_read.split(',')
#     file_fd.close()
#     with open('B.txt', 'w') as f:
#         f.write(list_str[0])
#     with open('C.txt', 'w') as f:
#         f.write(list_str[1])
#     with open('D.txt', 'w') as f:
#         f.write(list_str[2])

#--------------------------------------------------------------------
#最大子数组问题
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         tar_list = []
#         for i, val in enumerate(prices[1:]):
#             tar_list.append(val - prices[i-1])
#         #原问题转化为求解tar_list的最大子数组的问题
#         #动态规划思想:
#         """
#         假设f(i)表示第i天卖出获得的收益
#         a[i]作为一个子数组加入到f(i-1)中还是成为一个独立的子数组
#         if a[i] > f(i-1)+a[i]  则a[i]自成数组
#         a[i] < f(i-1) 则a[i]作为子数组加入到f(i-1)
#         """
#         _max = 0
#         temp = tar_list[0]
#         for i in tar_list[1:]:
#             temp = max(temp, i+temp)
#             _max = max(temp, max)
#         return _max

#--------------------------------------------------------------------
# class People:
#     def __init__(self, name: 'str' = '', age: '0<=int<=100' = 0) -> None:
#         self.__name = name
#         self.__age = age
#
#     def get_name(self) -> str:
#         return self.__name
#
#     def get_age(self) -> int:
#         return self.__age
#
#     def set_age(self, age: '0<=int<=100') -> None:
#         if age < 0 or age > 100:
#             print('data error')
#             return
#         self.__age = age
#
#     def set_name(self, name: 'str') -> None:
#         self.__name = name
#
#     def __repr__(self):
#         return f'{self.__name},{self.__age}'
#
# person1 = People('张三', 20)
# print(person1)
# person1.set_age(30)
# print(person1)
# person2 = People('李四', 30)
# print(person2)
# while True:
#     try:
#         num = int(input('输入一个数字\n'))
#     except ValueError as e:
#         print(f'异常信息为:{e}\n重新输入')
#     else:
#         print('没有发生异常')
#         break

#--------------------------------------------------------------------
#类的静态方法与其他方法的区别和调用规则
# class Animal:
#     name: str
#     _leg: str
#     def __init__(self, name: 'str' = '动物大家族', leg: 'str' = '四条腿'):
#         self.name = name
#         self._leg = leg
#     @staticmethod
#     def run():
#         print('动物们跑起来了')
#
# class Cat(Animal):
#     def __init__(self, name: 'str' = '波斯猫'):
#         Animal.__init__(self, name)
#     def playing(self):
#         print(f'{self.name}在玩耍')
#     def eat(self):
#         print(f'{self.name}在吃饭')
#     def __repr__(self):
#         return f'{self.name}'
#
# tom = Cat()
# tom.playing()
# tom.eat()
# tom.run()
# print(tom)

#--------------------------------------------------------------------
#判断文件是否存在，抛异常，抛自定义异常
# class OutOfAgeErr(Exception):
#     def __str__(self):
#         return f'Out of age'
#
# class IsOutAge:
#     def __init__(self, age: '0 < int < 100'):
#         if age < 0 or age > 100:
#             raise OutOfAgeErr
# try:
#     IsOutAge(102)
# except OutOfAgeErr as e:
#     print(f'错误信息：{e}')
# else:
#     print('No error')
# import os
# class IsFileExit:
#     def __init__(self, file_name: 'path str' = ''):
#         if not file_name:
#             self.file_name = input('输入文件名:\n')
#         self.file_name = file_name
#         try:
#             with open(self.file_name, 'r') as f:
#                 pass
#         except FileNotFoundError as e:
#             print(f'错误信息:{e}')
#
# IsFileExit('xxx.txt')

#--------------------------------------------------------------------
#子类重写父类方法以及调用规则
# class Father(object):
#     def eat(self):
#         print('I am father')
#
# class Son(Father):
#     def eat(self):
#         print('I am son')
#         super().eat()
#
# son = Son()
# son.eat()
# Father.eat(Father())

#--------------------------------------------------------------------
#能否访问和修改类私有属性
# class Name:
#     __name: str = 'wuyupeng'    #申明类时就已经在内存中占用空间？
#     def get_name(self):
#         return self.__name
#
# # print(Name.__name)  #被解释器遮挡了，没有这个变量
# # Name.__as = 'wuyupeng'
# Name._Name__name = 'donglinlin'   #成功修改
# print(Name.get_name(Name()))

#--------------------------------------------------------------------
#类变量，类私有变量的访问和修改
# class TestClass:
#     class_value = 2  #类变量，所有实例共享，所有实例都不可以改变
#     __private_value = 11  #类的私有实例变量，类外不可访问
#     uninit_val: str  #是否必须初始化？
#     @classmethod
#     def get_val(cls):  #类方法能访问类变量，实例方法也能访问
#         return cls.__private_value
#
#     def get_insval(self):   #实例方法能不能修改类变量？
#         return self.__private_value
#     # 实例方法能不能修改类变量？
#     def change_class_val(self):  #不可以，本质上是添加实例变量
#         self.__private_value = 19
#
# c = TestClass()
# print(c.class_value)
# c.class_value = 15  #实际上是给实例本身增加了一个实例变量
# print(c.class_value)
#
# c1 = TestClass()
# print(f'c1中的类变量值：{c1.class_value}')
#
# #那么类变量怎么去修改呢？通过类名访问
# TestClass.class_value = 3
# print(c1.class_value)   #已经改变了，并且可以用实例访问
#
# #怎么修改私有类变量？
# TestClass._TestClass__private_value = 12
# print(TestClass.get_val())  #观察私有类变量__private_value是否改变？输出12 改变了！！
# #观察实例方法能不能访问类变量
# print(c1.get_insval())
#
# c1.change_class_val()
# print(c1.get_val())
# print('='*10)
# # print(TestClass.uninit_val)     #抛异常AttrubuteError,解释器提示没有 uninit_val，说明python不支持这种声明变量的形式，这与python内的数据存储类型有关
# #python内部维护的其实都是指针/引用，并非变量本身
# addr = int
# print(addr)     #addr指向int类

#--------------------------------------------------------------------
#tuple里的列表可变吗？
# _tup = (1, 2, [3, 4])
# _tup[2] += [5, 6]
# print(_tup)   #抛异常 TypeError: 'tuple' object does not support item assignment
# _tup[2].append(5)   #尝试绕过异常，观察_tup到底有没有变
# print(_tup)     #还是抛异常 TypeError: 'tuple' object does not support item assignment
# _tup[2].extend([5, 6])
# print(_tup[2])    #绕不过去

#--------------------------------------------------------------------
#查看字节码
# dis.dis("s[a] += b")  #查看s[a] += b 背后的字节码

#--------------------------------------------------------------------
#可选函数
# list1 = ['asdf', '231', 'sfafee', 'e1r2341', 'a', 'bd']
# print(sorted(list1, key=len, reverse=False))  #sorted方法永远返回一个列表
#在内置函数里，有两个可选的关键字参数，reverse如果是True则代表降序排列
#key参数的作用是：
'''
一个只有一个参数的函数，这个函数会被用在序列里的每一个元素
上，所产生的结果将是排序算法依赖的对比关键字。比如说，在对一些
字符串排序时，可以用 key=str.lower 来实现忽略大小写的排序，或
者是用 key=len 进行基于字符串长度的排序。这个参数的默认值是恒
等函数（identity function），也就是默认用元素自己的值来排序。
实际上，在排序时，解释器是调用 len(_iter) > len(next(_iter))
进行比对排序的，类似C++中的函数指针
'''
#写一个实例如下
#函数名作为参数
# the_len = lambda x: len(x)
# def my_sort(val1, val2, *, key):
#     return val1 if key(val1) > key(val2) else val2
# print(my_sort('1341', 'dsfafaf', key=the_len))

#--------------------------------------------------------------------
#类中受保护的和私有的变量
# class Method:
#     _pro = 5  #受保护的
#     __private = 1  #私有的，被解释器遮挡，不能在外部访问
#
#     #当方法访问类属性时，解释器会提示这个方法 may be static
#     #当通过自身访问类属性时就不会，没有用self可能也会提示
#     def get_private(self):
#         return self.__private
#
# m = Method()
# b = m._pro
# print(b)
# print(Method._pro)
# print(Method.__private)

#--------------------------------------------------------------------
#os模块中的一些函数的用法
print(os.path.exists('python.txt'))
# os.makedirs('伍宇鹏的文件夹')
# os.removedirs('伍宇鹏的文件夹')


#--------------------------------------------------------------------
#sys模块中的一些内容和函数
# print(sys.version)  #查看版本信息
# print(sys.path)  #查看系统路径
# print(sys.float_info)  #查看浮点数范围
# print(sys.argv)  #命令行参数
# print(sys.getsizeof(int))  #查看int类的大小 416字节

# os.open()
#重置函数递归深度
# sys.setrecursionlimit(1000)
#
# datestamp = datetime(2022, 1, 22)
#
# s = pd.Series([1, 2, 3, 4])
# print(s)
# s = s * 2 + 1
# print(s)

#
# df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
# print(df.__dict__)
# df.columns = ['col1', 'col2', 'col3']
# print(df.__dict__)
# print(df)

# while True:
#     try:
#         cupNum = int(input())
#         cnt = 0
#         while cupNum > 1:
#             if cupNum == 2:
#                 cnt += 1
#                 break
#             k = cupNum // 3
#             cnt += k
#             cupNum = (k + cupNum % 3)
#             continue
#         print(cnt)
#     except:
#         break


print(eval(input()))


