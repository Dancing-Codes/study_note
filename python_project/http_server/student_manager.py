#面向对象设计
# import sys
# import os
from myException import *
from time import sleep  #, time
from random import randint
# from main import main
"""
学生类设计思路：
每个学生都特有的属性：name , age , tel, sex ...
学生是否有共有属性？在当前案例下，暂时没有
学生行为：
    1、说出自己的名字
    2、提供各种接口
    3、将自己封装成字典返回，以便数据存储
"""
class Student:

    def __init__(self, *, name= None, age: '0< int <100' = 0,
                 tel: str = None, sex: str = 'm') -> None:
        if not name:
            raise StudentNameIsNull()
        self.name = name
        # assert age < 0 or age > 100, "只有年龄在0~100之间才会正确设置，否则抛异常"
        if 0 <= age <= 100:
            self.age = age
        else:
            raise AgeError()
        # assert sex != 'm' or sex != 'w', '性别只能是w,m,否则抛异常'
        if sex == 'm' or sex == 'w':
            self.sex = sex
        else:
            raise SexError()
        self.__tel = tel

    def __str__(self):
        """
        打印一个学生对象时
        :return:
        """
        return f'姓名：{self.name},年龄：{self.age},性别：{self.sex},电话：{self.__tel}'

    def __eq__(self, other):
        """
        提供对比方法
        :param other:
        :return bool:
        """
        return True if other.name == self.name else False


    def speak_name(self):
        """
        说出自己的名字
        :return:None
        """
        return self.name

    def set_age(self, age: '0< int < 100'):
        """
        设置年龄
        :param age:
        :return None:
        """
        if 0 <= age <= 100:
            self.age = age
        else:
            raise AgeError()

    def set_sex(self, sex):
        if sex == 'w' or sex == 'm':
            self.sex = sex
        else:
            raise SexError()

    def set_tel(self, tel: str):
        self.__tel = tel

    def get_tel(self):
        return self.__tel

    def to_dic(self):
        """
        将自己打包成字典
        :return dic:
        """
        return {'name': self.name, 'age': self.age, 'tel': self.__tel, 'sex': self.sex}


"""
班级管理器类设计思路：
班级管理器特有属性：
    1、一个班级有多名学生
    2、每个班级都有编号和类型（如文科班，理科班等等）
班级管理器该有的方法：
    1、查询某个学生
    2、返回全部学生
    3、删除某个学生
    4、插入某个学生
    5、初始化数据
    6、将数据保存到文件
"""
IF_FIRST_TIME = False
class ClassManager:
    __FILE_NAME = 'stu_data.txt'

    def __init__(self):
        #如果是首次初始化，则创建一个空表
        #否则，从外部文件初始化数据
        self.students = []
        global IF_FIRST_TIME
        if IF_FIRST_TIME:
            IF_FIRST_TIME = False
        else:
            self.__init_data(ClassManager.__FILE_NAME)
        self.poem = ['东临碣石，以观沧海', '山重水复疑无路，柳暗花明又一村', '我寄愁心与明月，随风直到夜郎西', '君子见机，达人知命',
                     '落霞与孤鹜齐飞，秋水共长天一色', '宝剑锋从磨砺出，梅花香自苦寒来', '瀚海阑干百丈冰，愁云惨淡万里凝',
                     '山回路转不见君，雪上空留马行处', '春江潮水连海平，海上明月共潮生', '大漠孤烟直，长河落日圆',
                     '春花秋月何时了，往事知多少', '枯藤老树昏鸦，小桥流水人家', '沉舟侧畔千帆过，病树前头万木春',
                     '衣带渐宽终不悔，为伊消得人憔悴', '黄金百战穿金甲，不断楼兰誓不还', '生当作人杰，死亦为鬼雄',
                     '残雪凝晖冷画屏，落梅横笛已三更', '我是人间惆怅客，知君何事泪纵横', '寻寻觅觅，冷冷清清',
                     '红藕香残玉簟秋，轻解罗裳，独上兰舟']


    def __str__(self):
        return self.students

    def check_student(self, stu: Student) -> Student:
        if len(self.students) == 0:
            print('还没有任何学生！')
            return Student(name='NULL')
        for val in self.students:
            if val == stu:
                return val

    def delete_student(self, stu: Student):
        for i in self.students:
            if i == stu:
                self.students.remove(i)
                print('成功删除！3秒后返回主菜单')
                sleep(3)
                return
        else:
            print('No such student')
        return

    def insert_student(self, index: int, stu: Student):
        if abs(index) > len(self.students):
            print('index error')
            return
        else:
            self.students.insert(index, stu)
            print('插入成功！3秒后返回主菜单...')
            sleep(3)
        return

    def add_student(self, stu: Student):
        self.students.append(stu)
        print('添加成功！3秒后返回主菜单...')
        sleep(3)

    def all_student(self):
        for val in self.students:
            print(val)
            sleep(1)
        print(f'{self.poem[randint(0, len(self.poem)-1)]}，久等了呢~')

    def __init_data(self, filename: str) -> None:
        # if sys.path.exist(filename):
        with open(filename, 'r+') as file:
            str = file.read()
            students = str.split('\n')
        # else:
        #     raise FileNotFoundError()
        # 这里列表里存的是字符串还不是对象，必须把他们初始化为对象
        for i in students:
            # 先将i由字符串改成字典，在把字典改成对象，然后追加到列表里
            dic_stu = eval(i)
            self.students.append(Student(name=dic_stu['name'], age=dic_stu['age'], tel=dic_stu['tel']
                                         , sex=dic_stu['sex']))

    def store_data(self):
        temp = []
        #把列表里的对象修改成字典, 再把字典转换成字符串
        for i, val in enumerate(self.students):
            temp.append(str(val.to_dic()))
        with open(ClassManager.__FILE_NAME, 'w') as file:
            file.write(('\n'.join(temp)))
            print('数据保存成功，程序即将退出...')
            sleep(3)


    def __del__(self):
        # self.store_data()
        # del self.students
        pass

    def menu(self):
        while True:
            print('*-'*20)
            print('1、添加学生')
            print('2、删除学生')
            print('3、查找学生')
            print(f'4、修改学生\t\t{self.poem[randint(0, len(self.poem)-1)]}~')
            print('5、插入学生')
            print('6、所有学生')
            print('7、退出系统')
            print('*-'*20)
            flag = int(input())
            if flag == 1:
                name = input('输入要添加的学生姓名（必须设置）:')
                age = int(input('输入要添加的学生年龄:'))
                tel = input('输入要添加的学生电话:')
                sex = input('输入要添加的学生性别:')
                try:
                    self.add_student(Student(name=name, age=age, tel=tel, sex=sex))
                except (StudentNameIsNull, SexError, AgeError) as e:
                    print(f'您的某项输入出现了错误，错误信息为：{e}')
                    print('请重新选择您需要进行的操作，并认真校对相应的信息，即将返回主菜单...')
                    sleep(5)
                continue
            elif flag == 2:
                try:
                    self.delete_student(Student(name=input('要删除的学生名:')))
                except (StudentNameIsNull, SexError, AgeError) as e:
                    print(f'您的某项输入出现了错误，错误信息为：{e}')
                    print('请重新选择您需要进行的操作，并认真校对相应的信息，即将返回主菜单...')
                    sleep(5)
                continue
            elif flag == 3:
                try:
                    print(self.check_student(Student(name=input('要查找的学生名:'))))
                except (StudentNameIsNull, SexError, AgeError) as e:
                    print(f'您的某项输入出现了错误，错误信息为：{e}')
                    print('请重新选择您需要进行的操作，并认真校对相应的信息，即将返回主菜单...')
                    sleep(1)
                    print(f'{self.poem[randint(0, 9)]}')
                    sleep(5)
                else:
                    print('3秒后返回主菜单...')
                    sleep(3)
                continue
            elif flag == 4:
                print('暂未提供该功能，敬请期待...')
                print('即将返回主菜单...')
                sleep(3)
            elif flag == 5:
                name = input('输入要插入的学生姓名（必须设置）:')
                age = int(input('输入要插入的学生年龄:'))
                tel = input('输入要插入的学生电话:')
                sex = input('输入要插入的学生性别:')
                index = int(input('要插入的位置：'))
                try:
                    self.insert_student(index, Student(name=name, age=age, tel=tel, sex=sex))
                except (StudentNameIsNull, SexError, AgeError) as e:
                    print(f'您的某项输入出现了错误，错误信息为：{e}')
                    print('请重新选择您需要进行的操作，并认真校对相应的信息，即将返回主菜单...')
                    sleep(5)
                continue
            elif flag == 6:
                self.all_student()
                print('查询完成，5秒后返回主菜单...')
                sleep(5)
                continue
            elif flag == 7:
                self.store_data()
                print('海内存知己，天涯若比邻，再见~')
                break
            else:
                print('输入错误，请重新输入:')
                continue


#测试
if __name__ == '__main__':
    main()

    '''
    s1 = Student(name='伍宇鹏', age=21, tel='17674797554', sex='m')
    s2 = Student(name='董林林', age=24, tel='17424797254', sex='w')
    s3 = Student(name='陈嘉铭', age=25, tel='17274977454', sex='m')

    cmn = ClassManager()
    cmn.add_student(s1)
    cmn.add_student(s2)
    cmn.add_student(s3)

    cmn.store_data()
    del s1
    del s2
    del s3
    del cmn

    cln = ClassManager()
    '''
    # li = cln.all_student()
    # for i in li:
    #     print(i)
    # 测试通过^_^