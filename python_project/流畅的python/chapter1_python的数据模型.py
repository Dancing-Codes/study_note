import math
import sys
import os
#封装一个二维向量类，就是欧几里得空间里常用的那种向量
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    #向量的加法
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    #向量的数乘
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    #向量的模
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    #打印
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    #自定义的bool
    """
    默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对
    __bool__ 或者 __len__ 函数有自己的实现。bool(x) 的背后是调用
    x.__bool__() 的结果；如果不存在 __bool__ 方法，那么 bool(x) 会
    尝试调用 x.__len__()。若返回 0，则 bool 会返回 False；否则返回
    True。
    """
    #对bool的实现其实非常简单，只需要判断模长是否为零即可
    def __bool__(self):
        return bool(self.x or self.y)

#定义两个向量
v1 = Vector(3, 5)
v2 = Vector(1, 3)
#向量相加
v3 = v1 + v2
#打印一下v3向量
print(v3)
#v3向量乘以0.5
v3 *= 0.5
print(f"数乘后的v3:{v3}")

#在Python 语言参考手册中的“Data
# Model”（https://docs.python.org/3/reference/datamodel.html）一章列出了
# 83 个特殊方法的名字，其中 47 个用于实现算术运算、位运算和比较操
"""
类别              方法名
字符串         __repr__   __str__  __format__
字节序         __bytes__
数值转换        __abs__, __bool__, __complex__, __int__, __float__, __hash__, __index__
集合模拟        __len__, __getitem__, __setitem__, __delitem__, __contains__
迭代模拟        __iter__, __reversed__, __next__
可调用模拟       __call__
事实上，我的代码无需直接使用特殊方法，除非有大量的元编程存在，直接调用特殊方法的频率应该远远低于我实现他们的次数
唯一的例外是__init__和__del__方法，因为我在实例化或者析构对象时需要调用他们
python语言独特的口音：
    如果有其它语言的编程经验，或许会对 len(object)的写法感到不适，为什么不是object.len()或object.size()呢？
    当你进一步理解这种不适感背后的原因之后，会发现这个原因，和它所代表的庞大的设计思想，是形成我们通常说的“Python 风格”（Pythonic）的关
    键。这种设计思想完全体现在 Python 的数据模型上，而数据模型所描述的 API，为使用最地道的语言特性来构建你自己的对象提供了工具。
    数据模型其实是对 Python 框架的描述，它规范了这门语言自身构建模块的接口，这些模块包括但不限于序列、迭代器、函数、类和上下文管理器(with)。
    不管在哪种框架下写程序，都会花费大量时间去实现那些会被框架本身调用的方法， Python 也不例外。Python 解释器碰到特殊的句法时，会使
    用特殊方法去激活一些基本的对象操作，这些特殊方法的名字以两个下划线开头，以两个下划线结尾（例如 __getitem__）。比如 obj[key]
    的背后就是 __getitem__ 方法，为了能求得 my_collection[key] 的值，解释器实际上会调用 my_collection.__getitem__(key)。
    这些特殊方法名能让你自己的对象实现和支持以下的语言构架，并与之交互：
        迭代
        集合类
        属性访问
        运算符重载
        函数和方法的调用
        对象的创建和销毁
        字符串表示形式和格式化
        管理上下文（即 with 块）
    其实，这些方法都是自定义类默认继承object而得来的，这样的数据模型设计虽然带来了方便，但是消耗了很多的空间
"""
class MyClass:
    pass
print(sys.getsizeof(MyClass))   #一个空类在python里站1064个字节！

#为什么len不是普通方法
"实用胜于纯粹    ------《python值之禅》"
"""
如果 x 是一个内置类
型的实例，那么 len(x) 的速度会非常快。背后的原因是 CPython 会直接从一个 C 结构体里读取对象的长度，完全不会调用任何方法。获取一
个集合中元素的数量是一个很常见的操作，在str、list、memoryview 等类型上，这个操作必须高效。
换句话说，len 之所以不是一个普通方法，是为了让 Python 自带的数据结构可以走后门，abs 也是同理。但是多亏了它是特殊方法，我们也可
以把 len 用于自定义数据类型。这种处理方式在保持内置类型的效率和保证语言的一致性之间找到了一个平衡点，也印证了“Python 之禅”中的
另外一句话：“不能让特例特殊到开始破坏既定规则。”
"""
#《流畅的python》1.5章小结
"""
通过实现特殊方法，自定义数据类型可以表现得跟内置类型一样，从而
让我们写出更具表达力的代码——或者说，更具 Python 风格的代码。

Python 对象的一个基本要求就是它得有合理的字符串表示形式，我们可
以通过 __repr__ 和 __str__ 来满足这个要求。前者方便我们调试和
记录日志，后者则是给终端用户看的。这就是数据模型中存在特殊方法
__repr__ 和 __str__ 的原因。

对序列数据类型的模拟是特殊方法用得最多的地方，这一点在
FrenchDeck 类的示例中有所展现。在第 2 章中，我们会着重介绍序列
数据类型，然后在第 10 章中，我们会把 Vector 类扩展成一个多维的
数据类型，通过这个练习你将有机会实现自定义的序列。

Python 通过运算符重载这一模式提供了丰富的数值类型，除了内置的那
些之外，还有 decimal.Decimal 和 fractions.Fraction。这些数据
类型都支持中缀算术运算符。在第 13 章中，我们还会通过对 Vector
类的扩展来学习如何实现这些运算符，当然还会提到如何让运算符满足
交换律和增强赋值。
Python 数据模型的特殊方法还有很多，本书会涵盖其中的绝大部分，探
讨如何使用和实现它们。
"""