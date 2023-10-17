#定义上下文管理器
# from typing import overload  #重载装饰器

class File:
    def __init__(self, filename: str, filemode: str) -> None:
        self._filename = filename
        self._filemode = filemode

    def __enter__(self):
        print('进入上文函数')
        # 上下文管理器的上文函数
        self.__fd = open(self._filename, self._filemode)
        return self.__fd

    def __exit__(self, ex1, ex2, ex3):
        # 下文函数
        print('下文函数开始执行')
        print(ex1)
        print(ex2)
        print(ex3)
        self.__fd.close()
        return True  # 下文函数返回True表示函数内的异常已经处理了，不需要再传递给主程序

def test01():
    # with语句开始时会调用File的上文管理器（上文方法）
    with File('wuyupeng.txt', 'w') as f:
        print('with 语句开开始执行')
    # 结束时会调用File的下文管理器（下文函数）
    # 要是用上下文管理器必须实现__enter__和__exit__方法

def main():
    test01()


if __name__ == '__main__':
    main()
