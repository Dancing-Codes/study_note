from urllib import request
import pickle
#python文件IO操作
# 调用open函数可以返回一个file对象
# open(filename, mode)
# filename是文件名
# mode是打开方式
file = open('D:/wuyupeng.txt', 'w+')
"""
mode    description
r       以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
rb      以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头.
r+      打开一个文件用于读写。文件指针将会放在文件的开头。
rb+     以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w       打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb      以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+      打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
wb+     以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a       打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab      以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+      打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
a       以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
#测试用例
file.write('python 是一门很简单的语言\n')
file.write('真的吗？那我学学看\n')
file.writelines('是的，的确非常好')
file.close()

#文件对象的方法
"""1、file.read(size)"""  #这将读取一定的数据，然后作为字符串或字节对象返回
#size是个可选的数字类型参数，如果size被忽略了或者为负，那么该文件的内容都将被读取并且返回
file = open('D:/wuyupeng.txt', 'r+')
read_str = file.read(6)  #读取6个字符
print(read_str)     #输出python
#继续读取，看看文件指针是否发生改变
read_str = file.read(7)
print(read_str)  #文件指针发生了偏移！
"""2、readline()"""  #读取一行，文件指针便宜到下一行
read_str = file.readline()
print(read_str)
read_str = file.readline()
print(read_str)     #再读一行
"""3、readlines()"""  #返回文件的s所有的行,如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
lineCont = file.readlines()
print(lineCont)
"""4、write(string)"""  #将string写入文件中，返回写入的字符数,如果参数不是字符串，要先进行转换
print(file.write('，可以试试看呢'))
"""5、tell()"""  #返回文件对象当前所处的位置,它是从文件开始算起的字符数
print(file.tell())
"""6、seek(offset, from_what)"""   #改变文件指针当前的位置，offset表示偏移量，from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
file.seek(0, 0)  #将文件指针移动到文件开头
read_str = file.readlines()
print(read_str)
"""7、close()"""  #关闭文件

#str() --内置的将任意数据类型转换成字符串

#eval() --内置的将字符串转换成数据类型，看起来像什么就转成什么，但是字符串内定义的相应数据类型格式必须合法

#进阶进阶进阶进阶进阶
"""1、python 文件写入进行网络爬虫"""  #导包 from urllib import request
response = request.urlopen("https://www.baidu.com/")    #打开网站
fi = open('D:/python_req.txt', 'a+')
page = fi.write(str(response.readlines()))
fi.close()


"""2、数据的序列化和反序列化pickle模块"""
"""python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。"""
#写几个实例测试
data1 = {
    'a': {'name': '伍宇鹏', 'age': 21},
    'b': {'name': '陈嘉铭', 'age': 24},
    'c': {'name': '董小姐', 'age': 23}
}
output = open('D:/output.txt', 'wb')
pickle.dump(data1, output)          #把 data1 python对象中的数据序列化输出到output文件中，注意以二进制形式打开，以匹配任意文件类型
output.close()
_input = open('D:/output.txt', 'rb')
data2 = pickle.load(_input)     #将output文件中的内容序列化读入data2中，重构python对象
print(data2)

#拷贝案例


