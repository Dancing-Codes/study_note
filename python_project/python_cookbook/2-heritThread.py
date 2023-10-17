from threading import Thread
from time import sleep  #, time

"""
当线程被继承时，由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程
执行这样一个执行模型。所以，Python 的线程更适用于处理 I/O 和其他需要并发执行
的阻塞操作（比如等待 I/O、等待从数据库获取数据等等），而不是需要多处理器并行
的计算密集型任务。
"""
class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__(target=self.run)
        self.n = n

    def run(self) -> None:
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            sleep(2)
        print('子线程退出')

def test01():
    cdt1 = CountdownThread(5)
    cdt1.start()   #创建一个线程并执行run任务

def test02():
    #我们创建两个线程看他们是怎么执行的
    print('创建第一个子线程')
    cdt1 = CountdownThread(5)
    cdt1.start()  # 创建一个线程并执行run任务
    print('再创建一个子线程')
    cdt2 = CountdownThread(5)
    cdt2.start()

if __name__ == '__main__':
    # test01()
    # print('主线程退出')
    #运行结果
    """
    T-minus 5
    T-minus 4
    T-minus 3
    T-minus 2
    T-minus 1
    子线程退出
    主线程退出
    python中的线程是伪线程，主线程等待子线程退出才会退出
    线程是一个进程下的控制流，现代操作系统一般有许多的控制流
    所以一个进程下的所有线程都运行在进程的上下文中，当开启一个
    线程后，进程退化为主线程，主线程若是在子线程之前结束，那么
    当前进程的上下文就要被操作系统回收，那么其他没有执行完的线程
    也就没办法继续执行了，而python中的主线程会等待子进程结束再执行,
    为了探究原因，我们做如下test02测试用例，在test02内创建两个子线程，
    查看他们的执行情况
    """
    test02()
    #运行结果
    """
    创建第一个子线程
    T-minus再创建一个子线程
    5
    T-minus 5
    T-minus T-minus 44

    T-minusT-minus 3
    3
    T-minus 2
    T-minus 2
    T-minus T-minus 11

    子线程退出
    子线程退出

    Process finished with exit code 0

    """