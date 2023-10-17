
class StudentNameIsNull(Exception):
    """
    姓名为空异常
    学生姓名不能为空
    """
    def __str__(self):
        return '学生姓名不能为空！'

class SexError(Exception):
    """
    性别异常
    性别只能是男或女
    """
    def __str__(self):
        return '性别只能是 m：男 或 w：女！'

class AgeError(Exception):
    """
    年龄异常
    年龄范围0~100
    """
    def __str__(self):
        return '年龄范围 0~100 ！'

if __name__ == '__main__':
    # main()
    pass