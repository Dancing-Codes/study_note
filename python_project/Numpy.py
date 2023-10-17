import numpy as np
import pandas as pd
import seaborn as sb
"""
Numpy（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。
Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁的多。
Numpy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器
"""
score = np.array([
    [88, 22, 23, 67, 77],
    [88, 22, 23, 67, 77],
    [68, 52, 63, 76, 70],
    [48, 92, 83, 37, 72]
])
print(score)
print(type(score))

#ndarray的属性
"""
ndarray.shape   数组的维度
ndarray.ndim    数组的维数
ndarray.size    数组的元素数量
ndarray.itemsize 一个数组元素的长度（字节）
ndarray.dtype   数组元素的类型
"""
print(score.shape)
print(score.ndim)
print(score.size)
print(score.itemsize)
print(score.dtype)

# ndarray的数据类型
"""
np.bool
np.int8
np.int16
np.int32
np.int64
np.uint8
np.uint16
np.uint32
np.uint64
nd.float32
nd.float64
nd.complex
string_  字符串
unicode  Unicode编码的字符串
"""

#pandas的数据类型
"""
Pandas 是基于Numpy的，很多功能都依赖于Numpy的ndarray实现的，Pandas的数据类型很多与Numpy类似，属性也有很多类似；比如pandas数据中的NaN就是numpy.nan。
下图中为Pandas的数据类型清单，其中Categoricals 我们之前的学习中没有见过的：
Categoricals 是由固定的且有限数量的变量组成的。比如：性别、社会阶层、血型、国籍、观察时段、赞美程度等等。
categorical 类型的数据可以具有特定的顺序——比如：性别分为男、女，血型ABO；我们会在本章节的最后来了解这种数据类型。

object 
int64
float64
bool
datetime64
category
"""
dic = {
    'name': 'wuyupeng',
    'age': 21
}
df1 = pd.DataFrame(dic, index=[0], columns=['name', 'age'])
print(type(df1))
print(type(df1['age']))
print(type(df1['age'][0]))
print(type(df1['name'][0]))

# 我们再以seaborn包中自带的tips数据集为例，来具体查看数据类型
tips = sb.load_dataset('tips', data_home='C:\\Users\\wuyupeng\\Desktop\\data\\data')
print(tips.dtypes)
""" OutPut
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object
"""
tips.head()
