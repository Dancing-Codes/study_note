import keyword  # 导入工具包
# 总计153行代码，预计阅读时长7min
# 第一个python程序  python 字符串用双引号或单引号 python用缩进表示代码块
print("Hello python")

# 常用的快捷键
# ctrl + / 注释
# ctrl + alt + l 代码格式化
# ctrl + shift + F10 运行代码
# ctrl + d 复制光标所在行
# ctrl + y 删除光标所在行
# shift + enter 快速换行

"""
python 解释器
计算机不能直接理解除了机器语言以外的语言
比如C语言 -> 汇编语言 -> 机器指令

Cpython解释器
Jython解释器
PyPy
"""

# 1、变量
# python 中首次赋值变量会定义变量，再次定义变量会修改变量的值 本质是修改变量的指向
num = 123
print(num)
num = 257
print(num)
# python变量类型
'''
数字类型 int(整形)，float(浮点型)，bool(布尔型，用于判断true和false)，complex(复数型)
非数字类型 str(字符串)，List(列表)，tuple(元组)，set(集合)，dict(字典)
'''
# 定义变量，无需制定类型，自动推导
name = '小明'
age = 18
sex = True
height = 1.75
weight = 120

# type(变量名) 获取变量的类型，需要打印后才能看到
print(type(name))  # 输出结果为：<class 'int'>
print(type(age))

# 2、标识符
# 标识符的命名规则，区分大小写
"""
由字母、下划线和数字组成
不能以数字开头
不能和关键字同名
建议不要和类型同名，如：int，str
"""
"""
命名规范
    见名知意
    Python的命令规范建议变量、函数名都使用小写字母，多个单词用下划线 _ 来连接，如send_buf
    小驼峰式命名法（lower camel case）：
        第一个单词以小写字母开始；
        第二个单词的首字母大写，例如：myName、aDog
    大驼峰式命名法（upper camel case）
        每一个单字的首字母都采用大写字母，例如：FirstName、LastName
"""

# 3、关键字
# 导入工具包
# import keyword
# 打印关键字
print(keyword.kwlist)
"""
and     as      assert     break     class      continue    def     del
elif    else    except     exec      finally    for         from    global
if      in      import     is        lambda     not         or      pass
print   raise   return     try       while      with        yield
"""
# 4、输出
"""
在python中可以使用print函数将信息输出到控制台
如果希望输出文字信息的同时，一起输出数据，就需要用到格式化输出操作符
% 被称为 格式化操作符，专门用于处理字符串中的格式
包含 % 的字符串，被称为 格式化字符串
% 和不同的 字符 连用，不同类型的数据 需要使用 不同的格式化字符
%s	字符串
%d	有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用 0 补全
%f	浮点数，%.2f 表示小数点后只显示两位
"""
# 使用实例
# 1. 定义整数变量 student_no、age，字符串变量 name, 浮点型变量 height
student_no = 202101
student_name = '小鹏'
student_age = 21
student_height = 1.73
# 2. 输出：我是学号为000001的小鹏，年龄为21，身高为1.73米
print('我是学号为%06d的%s，年龄为%02d，身高为%.2f米' % (student_no, student_name, student_age, student_height))

# 5、输入
# 使用input获取键盘输入的数据,input函数是阻塞的
password = input("提示信息：请输入密码:")
print('您刚刚输入的密码是：%s' % password)

# 6、类型转换
"""
类型转换函数
int(x) ----->将x转换为一个整数
float(x) ----->将x转换为一个浮点数
str(x) ---->将x转换为字符串
"""
# 注意：浮点数形式的字符串无法转换为int，如int('1.5')会报错
# 类型转换代码示例
a = 123  # 整形int
a_str = str(a)
# 在终端打印a和a_str的数据类型
print('a的数据类型：%s,a_str的数据类型：%s' % (type(a), type(a_str)))

# 7、运算符
# 算术运算符+
"""
下面以 a=10, b=20 为例进行计算
运算符   描述     运算效果
+	    加	    两个对象相加 a + b 输出结果 30
-	    减	    得到负数或是一个数减去另一个数 a - b 输出结果 -10
*	    乘	    两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
/	    除	    b / a 输出结果 2
//	    取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
%	    取余	    返回除法的余数 b % a 输出结果 0
**	    指数	    a**b 为10的20次方， 输出结果 100000000000000000000
"""
# 注意：混合运算时，优先级顺序为： ** 高于 * / % // 高于 + - ，为了避免歧义，建议使用 () 来处理运算符优先级
# 代码示例
a = 5 / 2  # 5除以2，返回2.5，a的类型变为浮点数
print(a)
a = 5 // 2  # 5除2取整，返回2，a的类型变为整形
print(a)
a = 5 % 2  # 5除2取余，返回1，a的类型为整形
print(a)
a = 5 * 2   # 5乘2，返回10
print(a)
a = 5 ** 2  # 5的2次方，返回25
print(a)

# 赋值运算符
#    =	赋值运算符	把 = 号右边的结果 赋给 左边的变量，如 num = 1 + 2 * 3，结果num的值为7
# 示例代码
a = 2
a = a + 3
print(a)

# 复合赋值运算符
"""
运算符	    描述	        实例
+=	    加法赋值运算符	    c += a 等效于 c = c + a
-=	    减法赋值运算符	    c -= a 等效于 c = c - a
*=	    乘法赋值运算符	    c *= a 等效于 c = c * a
/=	    除法赋值运算符	    c /= a 等效于 c = c / a
%=	    取模赋值运算符	    c %= a 等效于 c = c % a
**=	    幂赋值运算符	    c **= a 等效于 c = c ** a
//=	    取整除赋值运算符	c //= a 等效于 c = c // a
"""
# 代码示例
a = 3
b = 7
print(b//a)
print(b % a)
