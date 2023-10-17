
from threading import Thread
from time import sleep
from socket import timeout
# 你要为需要并发执行的代码创建和销毁线程
# threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象。你可
# 以创建一个 Thread 对象并将你要执行的对象以 target 参数的形式提供给该对象
#一个简单的线程例子：
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        sleep(2)

def main():
    thread_1 = Thread(target=countdown, args=(5,))
    #启动一个线程进行数数
    thread_1.start()
    """
        当你创建好一个线程对象后，该对象并不会立即执行，除非你调用它的 start()
    方法（当你调用 start() 方法时，它会调用你传递进来的函数，并把你传递进来的参
    数传递给该函数）。Python 中的线程会在一个单独的系统级线程中执行（比如说一个
    POSIX 线程或者一个 Windows 线程），这些线程将由操作系统来全权管理。线程一旦
    启动，将独立执行直到目标函数返回。你可以查询一个线程对象的状态，看它是否还
    在执行：
    """
    while True:
        if thread_1.is_alive():
            print('thread is still running')    #主线程和子线程争抢CPU时间片，观察主线程是否比子线程打印更多的内容
            sleep(2)
        else:
            break
    thread_1.join()  #将一个线程加入到当前线程，阻塞等待子线程结束并回收其资源
    #对于长时间在后台运行的线程，可以设置成后台线程
    thread_2 = Thread(target=countdown, args=(5,), daemon=True)
    thread_2.start()

"""
    后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。除了如上所示的
两个操作，并没有太多可以对线程做的事情。你无法结束一个线程，无法给它发送信
号，无法调整它的调度，也无法执行其他高级操作。如果需要这些特性，你需要自己
添加。比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询
来退出。你可以像下边这样把线程放入一个类中
"""
class CountTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            sleep(1)

def test01():
    ct = CountTask()
    thread_3 = Thread(target=ct.run, args=(10,))
    #开始执行数数任务
    thread_3.start()
    #终止run任务，设置_running属性为False，由于run任务里的while每次都对_running进行轮询，所有能控制run方法的执行进度，这得益于线程执行在进程的上下文中
    ct.terminate()
    thread_3.join()
    #执行结果
    """
        可以看到，thread_3就执行了一次便退出了，一次后CPU时间片就被主线程给抢夺
    主线程抢夺CPU时间片后，立马向下执行，将_running属性设置为False，子线程抢夺
    CPU时间片后，对_running值进行轮询，发现为False立马退出，每次的轮询虽然浪费时间，但是
    给了主线程控制子线程的一种途径，但这样的途径也是有漏洞的
        如果线程执行一些像 I/O 这样的阻塞操作，那么通过轮询来终止线程将使得线程
    之间的协调变得非常棘手。比如，如果一个线程一直阻塞在一个 I/O 操作上，它就永
    远无法返回，也就无法检查自己是否已经被结束了。要正确处理这些问题，你需要利
    用超时循环来小心操作线程。例子如下：
    """
class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        #sock is a socket object
        sock.settimeout(5)  #设置一个超时属性，超过5秒，sock实例会抛出timeout异常
        while self._running:
            try:
                data = sock.recv(1024)
                break
            except timeout:  #捕获timeout异常，继续执行轮询
                continue
        return



if __name__ == '__main__':
    # main()
    #执行结果
    """
    T-minusthread is still running   print不是线程安全的！
    5
    T-minus 4
    thread is still running
    thread is still running
    T-minus 3
    T-minus 2
    thread is still running
    thread is still running
    T-minus 1
    显然，主线程争抢到了更多的cpu资源
    """
    test01()
