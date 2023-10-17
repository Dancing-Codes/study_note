#----------------包--------------
"""
包是一种管理python模块命名空间的形式，采用‘点模块名称’，直观上看，其就是一个文件夹的名称
比如一个模块的名称是A.B，那么他表示在这个包A中的模块B
就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库
不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。

现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。

并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。

这里给出了一种可能的包结构（在分层的文件系统中）:
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

"""
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
# import item  // from package.module import item // from module import *
# import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 :exc:ImportError 异常。
# 当我们使用 from package.subpackage import * 时发生了什么？
"""
Python 会进入文件系统，找到这个包里面所有的子模块，然后一个一个的把它们都导入进来。
但这个方法在 Windows 平台上工作的就不是非常好，因为 Windows 是一个不区分大小写的系统。
在 Windows 平台平台上，我们无法确定一个叫做 ECHO.py 的文件导入为模块是 echo 还是 Echo，或者是 ECHO。
为了解决这个问题，我们只需要提供一个精确包的索引。
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊
"""

# 包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，
# 你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。
# 这个功能并不常用，一般用来扩展包里面的模块。


###---------------关于OS模块的介绍---------------
#在前面已经学习了python文件IO，open函数返回一个file对象，file对象内维护了许多的文件操作方法，例如write，read等等
#在python中，还另外提供了文件操作模块OS，OS模块提供了非常丰富的方法用来处理文件个目录。常用的方法如下
#更多参考：https://www.runoob.com/python3/python3-os-file-methods.html
"""
    函数名称                                功能描述
1、os.access(path,mode)                  检验权限模式
2、os.chdir(path)                        改变当前工作目录
3、os.chflags(path,flags)                设置路径的标记为数字标记。
4、os.chmod(path,mode)                   更改权限
5、os.chown(path,uid,gid)                更改文件所有者
6、os.chroot(path)                       改变当前进程的根目录
7、os.close(fd)                          关闭文件描述符 fd
8、os.closerange(fd_low,fd_high)         关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9、os.dup(fd)                            复制文件描述符 fd
10、os.dup2(fd,fd2)                      将一个文件描述符 fd 复制到另一个 fd2
11、os.fchdir(fd)                        通过文件描述符改变当前工作目录
12、os.fchmod(fd,mod)                    改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13、os.fchown(fd,uid,gid)                修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14、os.fdatasync(fd)                     强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15、os.fdopen(fd,mode,bufsize)           通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16、os.fpathconf(fd,name)                返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17、os.fstat(fd)                         返回文件描述符fd的状态，像stat()。
18、os.fstatvfs(fd)                      返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
19、os.fsync(fd)                         强制将文件描述符为fd的文件写入硬盘。
20、os.getcwd()
21、os.getcwdb()
22、os.isatty(fd)
23、os.lchflags(path,flags)
24、
25、
26、
27、
28、
29、
30、
31、
32、
33、
34、
35、
36、
37、
38、
39、
40、
41、
42、
43、
44、
45、
46、
47、
48、
49、
50、
51、
52、
53、
54、
55、
56、
57、
58、
59、
60、
61、
62、
63、
64、
65、
"""
#==============================================================================================#

#+++++++++++++++++++++++++++++++++++++++++++测试用例+++++++++++++++++++++++++++++++++++++++++++++

#==============================================================================================#


#-------------------------PEP8: python代码风格指南-----------------------
#1. PEP8代码规范
# PEP8 提供了 Python 代码的编写约定，本节知识点旨在提高代码的可读性，并使其在各种 Python 代码中编写风格保持一致。
"""
1、缩进使用4个空格, 空格是首选的缩进方式. Python3 不允许混合使用制表符和空格来缩进.

2、每一行最大长度限制在79个字符以内.

3、顶层函数、类的定义, 前后使用两个空行隔开.

4、import 导入
    i:
        导入建议在不同的行
    ii:
        导包位于文件顶部, 在模块注释、文档字符串之后, 全局变量、常量之前.
        导入按照以下顺序分组:
            i：标准库导入
            ii:相关第三方导入
            iii:本地应用/库导入
            iv:在每一组导入之间加入空行
5、避免将小的代码块和 if/for/while 放在同一行, 要避免代码行太长.

6、永远不要使用字母 'l'(小写的L), 'O'(大写的O), 或者 'I'(大写的I) 作为单字符变量名. 在有些字体里, 这些字符无法和数字0和1区分, 如果想用 'l', 用 'L' 代替.

7、Python 中定义字符串使用双引号、单引号是相同的, 尽量保持使用同一方式定义字符串. 当一个字符串包含单引号或者双引号时, 在最外层使用不同的符号来避免使用反斜杠转义, 从而提高可读性

8、表达式和语句中的空格:
    i：避免在小括号、方括号、花括号后跟空格.
    ii：避免在逗号、分好、冒号之前添加空格.
    iii：冒号在切片中就像二元运算符, 两边要有相同数量的空格. 如果某个切片参数省略, 空格也省略.
    iv：避免为了和另外一个赋值语句对齐, 在赋值运算符附加多个空格.
    v：避免在表达式尾部添加空格, 因为尾部空格通常看不见, 会产生混乱.
    vi：总是在二元运算符两边加一个空格, 赋值（=），增量赋值（+=，-=），比较（==,<,>,!=,<>,<=,>=,in,not,in,is,is not），布尔（and, or, not

9、类名一般使用首字母大写的约定.

10、函数名应该小写, 如果想提高可读性可以用下划线分隔.

11、如果函数的参数名和已有的关键词冲突, 在最后加单一下划线比缩写或随意拼写更好. 因此 class_ 比 class 更好.(也许最好用同义词来避免这种冲突).

12、方法名和实例变量使用下划线分割的小写单词, 以提高可读性.

"""

#更多规范查看官网：
#   中文文档：https://www.python.org/dev/peps/pep-0008/
#   英文文档：http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/
