import numpy as np
from numpy.core import ndarray
from numpy import pi

# quick start
"""
NumPy 是 Python 科学计算的基础包。它是一个 Python 库，提供了一个多维数组对象、各种派生对象（例如掩码数组和矩阵）
，以及用于对数组进行快速操作的各种例程，包括数学、逻辑、形状操作、排序、选择、I/O 、离散傅立叶变换、基本线性代数、
基本统计运算、随机模拟等等。
"""

"""
NumPy 包的核心是ndarray对象。这封装了同构数据类型的n维数组，许多操作在编译代码中执行以提高性能。NumPy 数组和标准 
Python 序列之间有几个重要的区别：
1  与 Python 列表（可以动态增长）不同，NumPy 数组在创建时具有固定大小。更改ndarray的大小将创建一个新数组并删除原始数组。
2  NumPy 数组中的元素都需要具有相同的数据类型，因此在内存中将具有相同的大小。例外：可以拥有（Python，包括 NumPy）对象的数组，
   从而允许不同大小元素的数组
3  NumPy 数组有助于对大量数据进行高级数学运算和其他类型的运算。通常，与使用 Python 的内置序列相比，此类操作的执行效率更高，代码更少
4  NumPy 数组有助于对大量数据进行高级数学运算和其他类型的运算。通常，与使用 Python 的内置序列相比，此类操作的执行效率更高，代码更少
5  越来越多的基于 Python 的科学和数学包正在使用 NumPy 数组；尽管这些通常支持 Python 序列输入，但它们在处理之前将此类输入转换为 NumPy 数组，
   并且通常输出 NumPy 数组。换句话说，为了有效地使用当今大部分（甚至大部分）基于 Python 的科学/数学软件，仅仅知道如何使用 Python 的内置序列类型是不够的——还需要知道如何使用 NumPy 数组
"""
a = np.arange(100).reshape(10, 10)
b = np.arange(100).reshape(10, 10)
# 当使用Numpy进行大规模数据处理时，python表现出的速度并不那么让人满意
# NumPy 为我们提供了两全其美的优势：当涉及ndarray时，逐元素操作是“默认模式” ，但逐元素操作由预编译的 C 代码快速执行
c = a * b
# 以接近 C 的速度执行前面的示例所做的事情，但是我们期望基于 Python 的东西具有我们期望的代码简单性。事实上，NumPy 习惯用法更简单！
# 最后一个示例说明了 NumPy 的两个功能，它们是其强大功能的基础：矢量化和广播。

# 为什么Numpy快？
"""
向量化描述了代码中没有任何显式循环、索引等——当然，这些事情只是在优化的、预编译的 C 代码的“幕后”发生。矢量化代码有很多优点，其中包括：
矢量化代码更简洁易读
更少的代码行通常意味着更少的错误
代码更类似于标准的数学符号（通常更容易正确编码数学结构）
矢量化会产生更多的“Pythonic”代码。如果没有矢量化，我们的代码将充斥着低效且难以阅读的for循环。
"""
# 谁在使用Numpy
"""
NumPy 完全支持面向对象的方法，再次从ndarray 开始。例如，ndarray是一个类，拥有许多方法和属性。它的许多方法都由最外层 NumPy 命名空间中的函数镜像,
允许程序员以他们喜欢的任何范式进行编码。这种灵活性使 NumPy 数组方言和 NumPy ndarray类成为Python 中使用的多维数据交换的事实上的语言。
"""

# Numpy 快速入门
"""
NumPy 的主要对象是同构多维数组。它是一个元素表（通常是数字），所有类型都相同，由非负整数元组索引。在 NumPy 中，维度称为轴。
"""
# 构造一个ndarray
np_array: ndarray = np.arange(15).reshape(3, 5)
# 这是数组的轴数（维度）
print(np_array.ndim)
# 这是数组的维度.输出为（3,5）3行5列
print(np_array.shape)
# 这是数组中的数据类型 =>int32 numpy自带的数据类型
print(np_array.dtype)
# 这是数组中的每个元素大小
print(np_array.itemsize)
# 这是数组实际的缓冲区 输出缓冲区首元素的地址。这在C中非常关键，但在此我们并不关心，因为我们将使用索引来访问数组中的数据，通过向量化的方式来进行计算
print(np_array.data)

# array的创建方式
# 通过np.array创建，注意，这里的array和array.array中的array并不是一回事
a = np.array([2, 3, 4])
print(a)
# 也可以将序列转换为二维数组或者更高维度
b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)
# 像MATLAB那样创建一个全零数组3*5
c = np.zeros((3, 5))
print(c)
# 全1数组
d = np.ones([3, 5])
print(d)

# 为了创建数字序列，NumPy 提供了arange类似于 Python 内置的函数range，但返回一个数组
print(np.arange(0, 2, 0.1))  # 0 到 2以0.1为步长
# 也可以用linespace 获得更准确的精度
np.linspace(0, 2 * pi, 9)  # 9 numbers from 0 to 2
