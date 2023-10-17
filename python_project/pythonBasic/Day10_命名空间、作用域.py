import builtins
#官方文档的一段话
"""
A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries。
命名空间是从名称到对象的映射
"""
# 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系，所以一个命名空间中不嫩能有重名，但不同的命名空间重名是没有任何影响的
# 我们举一个计算机系统中的例子，一个文件夹中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同的文件夹中的文件可以重名

# 1、内置名称（built-in names）, python语言内置的名称，比如函数名、类名，变量名和异常类
# 2、全局名称（global names）, 模块中定义的名称，包括模块的变量，函数、类，其他导入的模块、模块级的变量和常量
# 3、局部名称（local names）, 函数中定义的名称
# 命名空间的查找顺序：局部变量->全局变量->内置命名空间
# 注意命名空间的生命周期

# 作用域
"A scope is a textual region of a Python program where a namespace is directly accessible" \
    "Directly accessible here means that an unqualified reference to a name attempts to find the name in the namespace."
# 作用域就是一个python程序可以直接访问命名空间的正文区域
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的
# 也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = 10
print(msg)   # msg并非局部变量，而是全局的,如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
"在函数内部访问全局变量可以使用 global"

# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量
print(dir(builtins))

# global和 nonlocal关键字
num = 10
def test():
    global num
    num = 123       # 这里在函数内更改了全局变量num的值
    print(f"全局变量num在函数里更改了的值:{num}")
test()
print(f"全局变量在函数外的值：{num}")

# 如果要修改嵌套作用域，则可以用nonlocal关键字声明
def outer():
    val = 10

    def inner():
        nonlocal val    # nonlocal关键字声明，访问外部变量val
        val = 100
        print(f"内层函数的val值：{val}")
    inner()
    print(f"外层函数的val值:{val}")
outer()