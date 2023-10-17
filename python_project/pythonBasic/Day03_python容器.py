# 总计490行代码，预计阅读时长60min+
# 1、列表 list---->[]
"""
列表(list)是python里最常使用的数据结构
专门用于存储一串数据，存储的数据称为元素,和其他强类型检测的语言不同（如：C++,Java），列表里的元素可以是任意数据类型
列表用 [] 定义，元素之间用,分隔
列表的正向索引从0开始依次递增，反向索引从-1开始依次递减
列表可以进行的操作：
    1、索引
    2、切片
    3、加
    4、乘
    5、检查成员
"""
list1 = ['伍宇鹏', 21, 'man']
##1.1、查看列表元素的数据类型
print(type(list1[0]))  # <class 'str'>
print(type(list1[1]))  # <class 'int'>
print(type(list1[2]))  # <class 'str'>
# 用列表存储的数据元素，其本身的数据类型不会改变!
# 现在，我们来格式化输出列表list1中的数据元素
print("姓名：%s，年龄：%d，性别：%s" % (list1[0], list1[1], list1[2]))

##1.2、列表索引和字段截取,左闭右开原则
# 用[]从列表中截取字段，list[i,j]表示从第i个开始，截取到第j个元素（包含i索引本身的元素，不包含j索引的元素）
list2 = list1[0:2]
print(list2)  # 输出 ['伍宇鹏', 21]
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])  # 输出 [10, 20, 30, 40]
# 用负数索引，list[i,-j]表示从第i个开始，截取到倒数第j个（不包含倒数第j个本身的元素）
list3 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
print(list3[1])  # 索引第二个元素Runoob
print(list3[1:-2])  # 输出['Runoob', 'Zhihu']

##1.3、列表运算操作
print(len(list3))  # 查看列表的长度/元素个数
list4 = list1 + list3  # 列表拼接
print(list4)  # 输出 ['伍宇鹏', 21, 'man', 'Google', 'Runoob', 'Zhihu', 'Taobao', 'Wiki']
print(['hello'] * 3)  # 列表乘  输出['hello', 'hello', 'hello']
print('伍宇鹏' in list1)  # 输出True
# 遍历表，基于范围的for循环
for x in list1:
    print(x)
# 截取和拼接可以复合使用

##1.4、嵌套列表
# 在列表里面嵌套其他表（list,tuple,dic,str字符串也可以看作是字符的表）
list5 = [list1, list3]
print(list5[0][0] == '伍宇鹏' and list5[1][0] == 'Google')  # 输出 True

## 1.5、列表的方法和增删改查
### 1.5.1、python中可以操作列表的函数&方法
"""
len(list)  返回列表的长度
max(list)  返回列表中的最大值
min(list)  返回列表中的最小值
list(tuple) 将元组转换为列表
"""
print(len(list1))  # 输出 3
# print(max(list1))  #输出 TypeError: '>' not supported between instances of 'int' and 'str'
# print(min(list1))  #同上，报错的原因是两个数据类型不同的元素之间没有合适的比较方法，在C++中的解决办法是运算符重载或者...


### 1.5.2、list面向对象和list容器(类)中的方法
# python底层的代码由C实现，其容器的很多特性非常类似于C++STL中的容器，其设计思想和面向对象思想不谋而合
# list容器(类)中封装的方法：
"""
list.append(obj)  在末尾添加新的元素
list.count(obj)  统计某个obj在列表中的出现次数
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新的列表扩展原来的列表）
list.index(obj)  索引obj在列表中的位置
list.insert(index,obj) 在index位置插入一个新元素obj
list.pop(obj=list[-1]) 删除list中的obj匹配项，默认删除最后一个 
list.remove(obj) 删除第一个obj的匹配项
list.reverse()  反转列表
list.sort(key = none, revers = False) 对原列表进行升序排序 sort(reverse=True)降序排序
list.clear()  清空列表
list.copy()  复制列表
"""
list_test = ['xiaomi', 'oppo', 'vivo', 'rongyao', 'huawei', 'iphone']
list_test.append(['iphone'])  # 追加表
list_test.append('iphone')  # 追加元素
print(list_test.count('iphone'))  # iphone的个数
print(list_test)  # 输出 ['xiaomi', 'oppo', 'vivo', 'rongyao', 'huawei', 'iphone', ['iphone'], 'iphone']

list_test.remove(['iphone'])  # 删除表中表
list_test.pop()  # 删除表中最后一个元素
print(list_test)  # 输出 ['xiaomi', 'oppo', 'vivo', 'rongyao', 'huawei', 'iphone']

list_test.insert(5, 'sanxing')  # 插入
list_test.reverse()  # 翻转
print(list_test)  # 输入['iphone', 'sanxing', 'huawei', 'rongyao', 'vivo', 'oppo', 'xiaomi']
## 进阶：列表整形数据元素的排序（选择排序，插入排序，快速排序，希尔排序，冒泡排序，堆排序，桶排序）

# --------------------------------------------------------------------------------------

# 2、元组 tuple----->()
"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改
可存储任意数据类型
元组使用小括号 ( )，列表使用方括号 [ ]
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
元组的正向索引从0开始依次递增，反向索引从-1开始依次递减
元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用
元组可以进行的操作：
    1、索引
    2、检查成员
"""
# 2.1、元组的基本操作
tuple1 = ('伍宇鹏', 21, '男')
# 元组索引和截取
print(tuple1[0])
print(tuple1[0:1])  # 从第零个开始，截取到第一个（不包括第一个）
print(tuple1[0:-1])  # 从第零个开始，截取到最后一个（不包括最后一个）

# 元组元素不能修改，但是可以组合、拼接、追加,实际上，python内部把原元组丢弃，开辟一块新的空间存储拼接后的对象
tuple2 = tuple1 + ('音乐',)
# ------------------------------------------------------------------------------------------------------------
######################*****************************************************************######################
# 关于元组元素是不可变的
# tuple1[0] = 'chenjiaming' 不支持
print(id(tuple1))  # 查看元组地址 输出1873807126976
tuple1 = (1, 2, 3)
print(id(tuple1))  # 再次查看元组地址 输出1873807340608，给整个元组重新赋值后变量绑定了新的地址
tupleX = (1, 2, 3)
print(id(tupleX))  # 查看tupleX的地址,输出1873807340608，tupleX和tuple1指向了相同的地址!!!
# 关于python中的数据存储方式的思考以及优缺点的讨论:
# 两个变量具有相同的值时，两个变量指向了相同的地址，可能python内部为这个地址维护着一个引用计数，当没有变量指向这个地址时，
# 这个地址才被释放（可用的）。在python里，一定区间内的整数或许早已被创建在内存中，当用户定义变量时，python检索比对
# 用户变量值和地址已存值，将用户变量映射到对应值的地址上。这样的数据存储方式在数据量较小时显得有点多此一举，浪费空间并且在比对变量值
# 和地址值时会浪费很多时间。但是，当python用来处理庞大的数据集时，这样的方式可以大大降低内存的消耗，同时还能相对高速地进行运算
# （因为值相同的变量地址也相同，CPU不需要频繁地进行寻址），并且，python把这些操作都封装到了底层，将复杂留给自己，简单留给用户，
# 让用户只去专注解决问题本身，而不需要考虑语言本身，甚至不需要知道它底层是怎样运作的。这些特性决定了python的应用领域，对庞大数据集
# 进行处理和运算，比如大型矩阵运算，卷积运算，回归分析，精度运算，方程离散等等，相对应的领域是人工智能、数据分析、数理统计、偏微分和数值逼近等等，
# 再回过头看python简介和应用领域，似乎一切本该如此。
######################*****************************************************************######################
# ------------------------------------------------------------------------------------------------------------
# 元组的值是不能被删除的，但是可以用del删除整个元组
del tuple2
# print(tuple2)  #输出 NameError: name 'tuple2' is not defined
# 查看元组元素的数据类型
print(type(tuple1[1]))  # 输出<class 'int'>

# 2.2、元组的运算操作
# 拼接
tuple3 = (1, 2, 3) + (4, 5, 5)
print(tuple3)
# 乘法
tuple4 = tuple3 * 2
print(tuple4)
# 判断元素是否存在
print(1 in tuple3)  # true
# 元组遍历
for x in tuple3:
    print(x)

# 2.3、python内置的可以操作元组的函数
"""
len(tuple)      计算元组元素的个数
max(tuple)      元组元素的最大值，当元组数据类型不一致时，无法比较
min(tuple)      元组元素最小值，当元组数据类型不一致时，无法比较
tuple(iterable) 将可迭代系列转换为元组（例如列表）
"""
print(len(tuple3))
print(max(tuple3))
print(min(tuple3))

# 2.4、元组类内封装的方法（类似列表）
"""
tuple.count(obj)  统计count出现的次数
tuple.index(obj)  返回obj在元组中的位置
"""
print(tuple3.count(5))
print(tuple3.index(3))

# --------------------------------------------------------------------------------------

# 3、字典 dic ----->{key:value}
# 字典是另一种可变容器模型，且可存储任意类型对象
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
# 键必须是唯一的(同一字典里不能出现相同的健key)，但值则不必。
# 键 key 是索引，值 value 是数据
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 一个简单的字典实例
dic = {"name": "伍宇鹏", "sex": "man", "age": 21}
dic1 = {'abc': 456}
dic2 = {'abc': 123, 98.6: 37}
print(dic)

# 3.1、字典的基本操作
# 访问
print(dic["name"])
# 修改
dic["name"] = "Runoob"
print(dic["name"])
# 删除
del dic["name"]  # 删除健name
dic.clear()  # 清空字典
print(dic)
del dic  # 删除字典
# 添加
dic1['love'] = 'music'  # 键不存在，则添加，键存在，则更新键值
if dic1['love'] is not None:
    pass
# 3.2、字典的特性
# 字典的值可以是任何python对象，也可以是用户自己定义的数据类型
# 两个重要的点需要记住
# 3.2.1、同一个键不能出现两次，在定义时出现两次，则保留最后的键值
dic_val = {'name': '伍宇鹏', 'name': 'Runoob'}
print(dic_val['name'])
# 3.2.2、键必须不可改变，所以可以用数字，字符串或元组充当，而用列表当键就不行，因为列表是可变的如下实例：
# dic_val = {['name']: '伍宇鹏'}  #TypeError: unhashable type: 'list'
# 3.2.3、字典的无限嵌套
cities = {
    '北京': {
        '朝阳': ['国贸', 'CBD', '天阶', '我爱我家', '链接地产'],
        '海淀': ['圆明园', '苏州街', '中关村', '北京大学'],
        '昌平': ['沙河', '南口', '小汤山', ],
        '怀柔': ['桃花', '梅花', '大山'],
        '密云': ['密云A', '密云B', '密云C']
    },
    '河北': {
        '石家庄': ['石家庄A', '石家庄B', '石家庄C', '石家庄D', '石家庄E'],
        '张家口': ['张家口A', '张家口B', '张家口C'],
        '承德': ['承德A', '承德B', '承德C', '承德D']
    }
}

# 3.3、python中可以操作字典的内置函数
"""
len(dic)    字典元素个数
str(dic)    将字典转换为字符串
type(val)   返回变量类型
"""
len(dic1)
str_val = str(dic1)
print("dic1字典长度：%d，字典转为字符串：%s" % (len(dic1), str_val))

# 3.4、字典类内封装的方法
""""
radiansdict.clear()     清空字典
radiansdict.copy()      浅拷贝
radiansdict.fromkeys(seq)   创建一个新的字典，以seq中的元素作为字典的键（注意元素重复和列表）  
radiansdict.get(key,default = none)     返回指定键的值，如果键不在字典中返回 default 设置的默认值
key in dic      如果键在字典dict里返回true，否则返回false
radiansdict.items()     以列表返回一个视图对象
radiansdict.keys()      返回一个视图对象
radiansdict.setdefault(key,default = none)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dic2)    把字典dict2的键/值对更新到dict里
radiansdict.values()    返回一个视图对象
pop(key[default])    删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
popitem()     随机返回并删除字典最后一对键值
"""
# 实例
dic_test = {'name': '伍宇鹏', 'sex': 'man', 'age': 21, 'favor': 'music'}
print(dic_test.keys())
print(type(dic_test.items()))
print(dic_val.keys())
# 删除key所对应的键值对
dic_test.pop('favor')
print('删除后:', end='')
print(dic_test)
# 浅拷贝
dic_val = dic_test.copy()
print('dic_test的地址: %d' % id(dic_test))
print('dic_val的地址: %d' % id(dic_val))

# --------------------------------------------------------------------------------------

# 4、字符串 str
# 字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串
# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用
"""
字符串支持的操作
1、索引
2、拼接、截取、加
3、遍历
4、乘
5、查找
"""
##1、基本操作
# 创建一个字符串
my_str = 'python'
#         012345
#       -5-4-3-2-1
# 索引
print(my_str[0])
# 遍历
for val in my_str:
    print(val, end='')
# f-strings字符串格式化
# f-strings是Python 3.6之后的一种新的字符串格式化方法，要使用f-strings，只需在字符串前加上f、或F：
name = 'wuyupeng'
age = 21
sex = 'male'
# 传统格式化输出
print('我叫%s,今年%d，%s' % (name, age, sex))
# f-strings格式化
print(f'我叫{name},今年{age},{sex}')
# 乘
print(name * 2)
# 查找
print('c' in my_str)

##2、python转义字符
# '\' 在行尾表示续行符,在字符串内表示转义
print("\\")  # 这是一个反斜杠
print("\'")  # 这是一个单引号
print("\"")  # 这是一个双引号
print('\a')  # 响铃
print("\n")  # 换行
print("\b")  # 退格
print("\t")  # 纵向制表符
print("\v")  # 横向制表符
print("\r")  # 回车 将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成
print("\f")  # 换页
print("\000")  # 空
print("\110\145\154\154\157\40\127\157\162\154\144\41")  # 八进制数,输出 Hello World
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")  # 十六进制数 输出 Hello World

##3、字符串运算符
"""
+           字符串连接
*           重复输出字符串
[]          索引
[:]         截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。
in          成员运算符 - 如果字符串中包含给定的字符返回 True
not in      成员运算符 - 如果字符串中不包含给定的字符返回 True
%           格式字符串
r/R         原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法
"""
# 写一些测试用例
str_test = 'hello'
print(str_test + 'world')
str_test += 'world'
str_test *= 3
print(str_test[0:5])
print('h' in str_test)
print('x' not in str_test)
print(r'你好\hello')

##4、Unicode字符串/Unicode字符集
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串

##5、python三引号
# python三引号允许一个字符串跨多行，字符串中可以包含换行符，制表符以及其他特殊字符
parameter_str = """ 这是一个多行字符串实例
多行字符串可以使用制表符
tab(\t)
也可以使用换行符[\n]
"""
print(parameter_str)

## 6、字符串内建函数
"""
^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^
    ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     
        ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^
            ^_^     ^_^     ^_^     ^_^     ^_^     ^_^     ^_^
                ^_^     ^_^     ^_^     ^_^     ^_^     ^_^
                    ^_^     ^_^     ^_^     ^_^     ^_^
                    ^_^                             ^_^
                    ^_^    --|--           --|--    ^_^
                    ^_^                             ^_^             南无阿弥陀佛，人生苦短，勿入码海~
                    ^_^              |              ^_^     
                    ^_^              |              ^_^    
                    ^_^                             ^_^
                    ^_^            ~~~~~            ^_^
                    ^_^                             ^_^
find(目标字符串，开始索引，结束索引)  查找，成功返回第一个字符的索引，不存在返回-1
replace(原内容，新内容，替换次数)  替换，字符串不能更改，所以返回一个新的被替换的字符串
split(分隔符) 以分隔符分割字符串，不填参数则默认以空格分割，返回一个含字符串的列表
字符串.join(目标表)   使用字符把指定表拼接起来
count(target,__begin,__end)  统计某个字符或串出现的次数
"""
# 测试用例
str1 = 'abc python'
print(str1.find('abc'))
new_str = str1.replace('abc', 'hello', 1)
print(new_str)
split_list = str1.split(' ')
print(split_list)
new_str = ':'.join(split_list)  # 使用:拼接
print(new_str)

# 7、字符串切片强化~~~~列表、元组也能切片
str_test = 'python'
# 字符串逆序
print(str_test[::-1])  # 注意截取的方向
print(str_test[6:1:-1])
print(str_test[6::-2])

# --------------------------------------------------------------------------------------

# 5、集合 set----->{}
# 集合（set）是一个无序的'不重复'元素序列  ---可以将列表转为集合完成去重功能，集合本身是无序的，所以不能通过[index]索引
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
parameter_set = {'apple', 'banana', 'orange', 'pear'}
# 话不多说，开始整活儿
##5.1、集合的基本操作
###5.1.1、添加元素
parameter_set.add('iter')
# 如果元素已存在，则不进行任何操作
parameter_set.add('apple')
print(parameter_set)
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
parameter_set.update(list1)  # value 可以有多个，用逗号分开。
print(parameter_set)  # 输出{'man', 'iter', 'banana', '伍宇鹏', 'apple', 21, 'pear', 'orange'},已经排好序？？不确定就写个测试用例试一下^^
test_set = {33, 1, 5, 7, 2, 133, 34}
print(test_set)  # 并没有排好序……
###5.1.2、删除元素
test_set.remove(1)
test_set.remove(2)
# 还可以这样删
test_set.discard(5)
# 我们也可以设置随机删除集合中的一个元素，语法格式如下：
test_set.pop()
print(test_set)  # 输出 {34, 133, 7} 随机删掉了33，哈哈^^~3333333333.......但好像并不是这样...
#                  set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除!
###5.1.3、索引/遍历
# print(parameter_set[1])   集合不支持【】索引
for val in parameter_set:
    print(val, end=',')
###5.1.4、拼接/查找某元素
# print(parameter_set + test_set) 集合没有重载+号和*号运算符，下文有提供交并函数
print(133 in test_set)

##5.2、函数函数函数
"""
set.add(item)  为集合添加元素
set.clear()   清空集合
set.copy()    拷贝集合（浅拷贝）
set.pop()           随机移除一个元素，返回移除的元素
set.remove(item)    移除某个元素，没有返回值
set.difference(set1)    返回多个集合的差集，返回值为一个新的集合，是多个集合彼此互不相交的部分
set.difference_update(set1) 移除集合中的元素，该元素在set1中也存在,移除相交部分
set.discard(value)      删除集合中的指定元素       
set.intersection(set1)      返回集合的交集
set.intersection_update(set1) 在set中移除set1中没有的元素,即移除不相交部分，保留相交部分
set.issubset(set1)      判断指定集合是否为该方法参数集合的子集，返回值True False
set.issuperset()    判断该方法的参数集合是否为指定集合的子集
set.union()         返回两集合的并集
set.update()        给集合添加元素
set.symmetric_difference(set1) 返回一个新集合是两个集合中不相交的部分 
set.symmetric_difference_update(set) 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
"""
# 测试案例
test_set = {1, 2, 3, 4, 5, 66, 234, 532, 2451, 3}
print(test_set)  # 集合中不能有重复的元素
# 添加元素
test_set.add(77)
print(test_set)
# 拷贝集合
test_set2 = test_set.copy()
print(test_set2)
# 移除某个元素
test_set2.remove(77)
print(test_set)  # 虽然是浅拷贝，但是删除test_set2中的77后查看test_set中的值，发现77还在test_set中，若有所思...
# 求差集,返回一个x集合中有，y集合中没有的集和
x = {'apple', 'banana', 'orange'}
y = {'apple', 'google'}
z = x.difference(y)
print(z)  # {'orange', 'banana'}
# 减去交集 在test_set中减去相交部分
test_set.difference_update(test_set2)
print(test_set)
# 求集合的交集,返回一个新的集合
new_set = test_set.intersection(test_set2)
print(new_set)  # 输出空集set()
# 在原集中移除不相交的部分set.intersection_update(set1, set2 ... etc)
test_set.add(1)  # 此时test_set = {77,1}
test_set.intersection_update(test_set2)  # 移除77
print(test_set)  # {1}
# 判断你是否是我的子集
test_set.issubset({1})
# 判断我是否是你的子集
test_set.issuperset(test_set2)
# symmetric_difference的使用
x = {1, 2, 3}
y = {2, 4, 5}
z = x.symmetric_difference(y)
print(z)  # {1, 3, 4, 5}
# symmetric_difference_update的使用
x = {1, 2, 3}
y = {2, 4, 5}
x.symmetric_difference_update(y)
print(x)  # x = {1, 3, 4, 5}
