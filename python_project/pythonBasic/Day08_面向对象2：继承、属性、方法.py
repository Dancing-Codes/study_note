#类中的__init__(self)构造方法，在实例化一个类是会自动调用
# 当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
class MyClass:
    def __init__(self):   #不能在构造方法的外部初始化实例变量
        print('类的构造方法调用')
        self.my_name = '伍宇鹏'

    def get_my_name(self):
        return self.my_name

# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。类似this指针
class MyClass0:
    def prt(self):
        print(self)
        print(self.__class__)
class_test = MyClass0()
class_test.prt()
#输出结果如下
# <__main__.MyClass0 object at 0x0000021BC6ADC040> self代表类的实例，代表当前对象的地址
# <class '__main__.MyClass0'> 而self.class指向类，self不是关键字，所以可以用其他任何标识符替代
class Test:
    def __init__(runoob):
        print(runoob)
        print(runoob.__class__)
t = Test()
t.__init__()

#继承,子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
#BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
#python继承语法如下
class People:
    #定义类属性，所有对象共有
    # 类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有。
    # 定义在类里面，类方法外面的变量就是类属性，类属性可以使用类名或实例对象访问，推荐使用类名访问
    name = ''
    age = -1
    #定义私有属性，私有属性类外无法直接访问
    __weight = -1
    #定义构造方法
    def __init__(self, name, age, __weight):
        self.name = name
        self.age = age
        self.__weight = __weight
    #定义类的行为（方法）
    def speak(self):
        print('我叫%s,今年%d,体重%dkg' % (self.name, self.age, self.__weight))
#单继承实例
class Student(People):
    class_no = -1
    grade = ''
    def __init__(self, name, age, weight, class_no, grade):
        #调用父类的构造函数
        People.__init__(self, name, age, weight)
        self.class_no = class_no
        self.grade = grade
    #重写（覆盖写）父类方法
    def speak(self):
        print('我叫%s，今年%d，在%d班，在读%s年级' % (self.name, self.age, self.class_no, self.grade))

s = Student('wuyupeng', 20, 56, 155, '高三')
s.speak()

#多继承
#python支持有限的多继承形式
#class sunclass(base0,base2,base3)
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
# 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
class Speaker:
    language_grade = ''
    name = ''
    def __init__(self, name, language_grade):
        self.name = name
        self.language_grade = language_grade
    def speak(self):
        print(f'我叫{self.name},是一个演说家，普通话等级是{self.language_grade}')
class SpeakerWorker(Student, Speaker):
    def __init__(self, name, age, class_no, grade, language_grade):
        Student.__init__(self, name, age, '56', class_no, grade)
        Speaker.__init__(self, name, language_grade)
test = SpeakerWorker('Tom', 24, 145, '三', '八')
test.speak()   #此处调用的是Student类中的方法


#方法重写(override)
#如果父类中的某些方法子类中满足不了需求，可以对父类方法进行重写
class Parent:
    def my_method(self):
        print('调用父类方法')
class Child(Parent):
    def my_method(self):
        print('调用子类方法')
c = Child()
c.my_method()
#在子类中调用父类中以及被覆盖的方法
#super类
super(Child, c).my_method()

#关于子类继承父类构造函数的进一步说明
# 如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
# 子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__
# 子类重写__init__，而且从父类继承的属性也必须初始化，或者在构造函数里调用父类构造函数初始化父类属性
# 在Java和C++中，子类不管有没有构造函数，子类实例化对象时都会调用父类的构造函数，还可以把子类构造函数的参数抛给父类构造函数
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
class Son(Father):
    def __init__(self, name):  #如果不对父类属性进行初始化，会提示init of super class is missed
        self.my_name = name    #这是子类中和父类同名的属性还是父类中被子类继承的属性？
        #重写了构造方法，也可以调用父类构造方法把继承的一些父类属性也给初始化，也可以用super调用
        Father.__init__(self, '父类名字', 73)
    def get_name(self):
        print(f'从父类中继承的属性：{self.name},{self.age}，自有属性{self.my_name}')
s = Son('wuyupeng')
s.get_name()


#类的属性和方法, 属性和变量类似，首次赋值时会定义属性，再次赋值改变属性
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods


#运算符重载
#python同样支持运算符重载，只是这些重载函数名已经被python默认加到类中了，就是前文提到的类的专有方法，对他们进行重载就行了
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    #打印方法重载
    def __str__(self):
        return 'Vector (%d,%d)' % (self.a, self.b)
    #加法重载
    def __add__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        return Vector(self.a, self.b)
v1 = Vector(1, 3)
v2 = Vector(2, 4)
print(v1 + v2)
print(v1)

#多态
# 多态：多种形态，调用同一个函数，不同表现
# 因为Python是动态语言，站在用户的角度，本身就是多态，不存在非多态的情况
# 实现多态的步骤:
# 实现继承关系
# 子类重写父类方法
# 通过对象调用该方法

#类方法 使用@classmethod修饰


#静态方法 使用@staticmethod修饰
