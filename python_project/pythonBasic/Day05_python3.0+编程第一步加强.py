# 组包和拆包
# 组包
res = 10, 20, 30  # 将左侧三个数封装到一个元组中
# 拆包
a, b, c = res  # 将res中的元素拆封，注意元素个数的匹配，除了对元组进行拆包以外，还可以对列表和字典进行拆包。
# 应用场景
# 1、交换变量的值
a, b = b, a     # 先自动组包，然后自动拆包
# 2、函数可以多次返回多个数
def return_agr():
    return 1, 2, 3  # 返回一个元组，自动组包
a, b, c = return_agr()  # 拆包
#字典元素的拆包
info_dict = {'name': 'wuyupeng', 'age': 21}
#先遍历字典，取出每一个item
i_type = type(info_dict.items())
print(f'items函数的返回值类型{i_type}')  #<class 'dict_items'>
for item in info_dict.items():  #以列表的形式返回一个视图对象，此处注意代码优化
    print(item)     #元组:(key: value)
    key, value = item  #元组拆包
    print(key, value)

#range的使用,range方法可以返回一个整数列表对象，一般用在for循环中，range(开始，结束，步长) 和切片方法差不多
for i in range(1, 5):  #左闭右开原则
    print(i)

#列表推导式
#快速生成列表元素的表达形式，通过for添加列表元素的简介写法
#推到的基本格式：[计算公式 for 循环 if 判断]
#每循环一次，将哦那个是的结果添加到列表中
#计算公式可以使用遍历出的数据
#for遍历出的数据必须满足if判断，然后才会使用计算公式生成元素
#写一个实例
new_list = []
for val in range(1, 5):  #将1~4添加到new_list中
    new_list.append(val)
print(new_list)
#上述写法也可以这样
new_list1 = [i for i in range(1, 5)]
print(new_list == new_list1)
# 将0~100里所有的质数添加到列表中
new_list2 = [i for i in range(0, 101) if i % 2 == 0]
print(new_list2)


a = 10 if new_list2.index(10) else 20

#匿名函数
#匿名函数是普通函数的简单写法
#定义的函数没有名字，这样的函数成为匿名函数，在C++中为lambda表达式
#格式 lambda [形参1],[形参2],...: [单行表达式]或[函数调用]
a, b = 3, 7
max_num = (lambda arg1, arg2: arg1 if arg2 > arg2 else arg2)(a, b)  #直接调用匿名函数
print(max_num)
max_func = lambda arg1, arg2: arg1 if arg1 > arg2 else arg2   #给匿名函数起名字，再调用，实际上，并不推荐使用这种方法，因为要如此的话，直接def就好了
print(max_func(a, b))
#函数作为函数的参数（类似C++中的函数指针）
# 对两个数进行任意func操作
def foo(value1, value2, func):
    return func(value1, value2)

# enumerate 的使用
#通过for配合enumerate遍历容器同时获取元素索引位置、元素
u_list = [{'name': 'wu', 'age': 21},
          {'name': 'chen', 'age': 25}, [1, 2, 3]]
for i, u_info in enumerate(u_list):
    print(i, u_info)    #0 {'name': 'wu', 'age': 21} 1 {'name': 'chen', 'age': 25} 2 [1, 2, 3]
    #事实上，enumerate是一个类，调用其构造方法传入参数，可以将容器元素逐个拆分并且保存索引位置，这里涉及到类封装的高级知识，类似C++中的重载了()的类
    #这里也有拆包的操作

#案例
#学生名片管理系统，先用容器存储数据，后续接触到python MySQL时再使用数据库存储数据同时使用面向对象思想封装数据
#1、容器设计思路分析：
#首先，对于某一个同学，为他维护一张名片，名片中可以包含许许多多的信息，例如name,age等等，显然，我们可以使用字典来进行封装
#其次，对于一个班级，有着许许多多的同学，所以，把字典（名片）封装到列表中,索引值+1代表第几位同学,方便查询
#又，对于一个学校，有多个班级，每个班级应当为其维护一些信息，例如班级所属年级，班级编号，班级属性（文理科，艺术音乐等等）和学生等等,用字典来封装班级
#学校本身可以看作一些班级的集合/列表表出各个班级，方便索引、插入、修改等操作
# 综上所述,将容器设计成如下形式:
# [{'classGrade': '高一', 'classNo': 2103, 'classType': '理科', 'students':[{'name':'w','age':21},{}...]},
#  {'classGrade': '高二', 'classNo': 2002, 'classType': '文科', 'students':[{'name':'c','age':24},{}...]},
#  {},...]
#2、面向对象存储数据的代码实现（本案例不使用此面向对象封装思想）:
class Student:
    pass
class Class:
    pass
class School:
    pass
#3、需要实现的功能模块：增、删、改、查、退出
#代码
my_school = []
class1 = {'classGrade': '高一', 'classNo': 2103, 'classType': '理科'}
class2 = {'classGrade': '高二', 'classNo': 2002, 'classType': '文科'}
class3 = {'classGrade': '高三', 'classNo': 1903, 'classType': '理科'}
class4 = {'classGrade': '高三', 'classNo': 1903, 'classType': '艺术'}
student1 = {'name': '孙悟空', 'age': 21, 'phone': 13722137871}
student2 = {'name': '妲己', 'age': 21, 'phone': 13722137823}
student3 = {'name': '亚瑟', 'age': 22, 'phone': 13722132327}
student4 = {'name': '苏烈', 'age': 22, 'phone': 13722112343}
student5 = {'name': '安琪拉', 'age': 23, 'phone': 13722153534}
student6 = {'name': '诸葛亮', 'age': 23, 'phone': 13722133433}
student7 = {'name': '李元芳', 'age': 24, 'phone': 13722133535}
student8 = {'name': '李白', 'age': 23, 'phone': 13722133435}

class1['students'] = [student1, student2]
class2['students'] = [student3, student4]
class3['students'] = [student5, student6]
class4['students'] = [student7, student8]

my_school.append(class1)
my_school.append(class2)
my_school.append(class3)
my_school.append(class4)

#查学生,可重载多个版本
def find_student():
    pass
#修改学生信息,可重载多个版本
def change_student_info():
    pass
#插入一个学生,可重载多个版本
def insert_student():
    pass
#删除一个学生,可重载多个版本
def delete_student():
    pass
#查班级,可重载多个版本
def class_info():
    pass
#修改班级信息,可重载多个版本
def class_change():
    pass
#插入班级,可重载多个版本
def class_insert():
    pass
#删除班级,可重载多个版本
def class_delete():
    pass
#菜单打印
def menu():
    while True:
        print('='*25)
        flag = int(input('1、对班级操作，2、对学生操作，3、退出'))
        if flag == 1:
            while True:
                sub_flag = int(input('1、查班级，2、修改班级信息，3、插入班级、4、删除班级，5、返回上一级，6、直接退出'))
                if sub_flag == 1:
                    class_info()
                elif sub_flag == 2:
                    class_change()
                elif sub_flag == 3:
                    class_insert()
                elif sub_flag == 4:
                    class_delete()
                elif sub_flag == 5:
                    break
                elif sub_flag == 6:
                    print('感谢使用')
                    return
                else:
                    print('输入有误，请重新输入')
                    continue
        elif flag == 2:
            while True:
                sub_flag = int(input('1、查学生，2、修改学生信息，3、插入一个学生、4、删除一个学生，5、返回上一级，6、直接退出'))
                if sub_flag == 1:
                    find_student()
                elif sub_flag == 2:
                    change_student_info()
                elif sub_flag == 3:
                    insert_student()
                elif sub_flag == 4:
                    insert_student()
                elif sub_flag == 5:
                    break
                elif sub_flag == 6:
                    print('感谢使用')
                    return
                else:
                    print('输入有误，请重新输入')
                    continue
        elif flag == 3:
            break
        else:
            print('输入错误，请重新输入')
            continue
    print('感谢使用信息管理系统!')
    return


# python 迭代器和生成器
# 类似于C++STL中的迭代器，但不同的是python迭代器不允许用户私自操作，只能调用系统提供的接口来操作迭代器，系统只让迭代器往前走
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象，这与C++迭代器不谋而合，若容器已经销毁，迭代器失效，注意非法访问错误
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。iter()用于创建迭代器对象，next()用于后移迭代器
# 已经知道，set是无序不重复的集合，由于其无序性，所以不能试图通过[]进行访问，因为在逻辑上，它是无序的，但是在物理地址上，他元素的存储是有序的！
# 字符串，列表或元组对象都可用于创建迭代器：
set1 = {1, 2, 4, 55, 33, 32}
set_iter = iter(set1)  # set_iter迭代器对象是set1的一个指针！
print(set_iter)  # <set_iterator object at 0x0000029492A04880 ----->set1第一个元素的首地址>
print(next(set_iter))


