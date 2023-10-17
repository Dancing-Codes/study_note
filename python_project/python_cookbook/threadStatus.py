from threading import Thread, Event, Condition, Semaphore
from time import time, sleep
# from typing import overload
#问题：你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了。
"""
线程的一个关键特性是每个线程都是独立运行状态不可预测。如果程序中的其他线程需要通过判断某个线程的状态
来确定自己下一步的操作，这时，线程同步的问题就变得非常棘手。为了解决这个问题，我们需要使用threading库中的
Event对象。Event对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初始情况下，event对象的
标志为假，那么这个线程将会一直阻塞直到该标志为真。一个线程如果将一个event对象的信号标志为真，它将唤醒所有等待
这个event对象的线程。如果一个线程等待一个已经被设置为真的event对象，那么它将忽略这个事件，继续执行。
下面代码展示如何使用event来协调线程的启动
"""
def countdown(n: int, started_evt: Event):
    print('countdown starting')
    #给所有等待event事件的线程发送信号
    started_evt.set()  #将Event设置为True，等待Event的线程都将被启动
    while n > 0:
        print('T-minus', n)
        n -= 1
        sleep(2)

def test01():
    #创建一个事件对象
    ev = Event()
    thread_1 = Thread(target=countdown, args=(5, ev))
    thread_1.start()
    #主线程等待事件信号
    ev.wait()
    print('countdown is running')

"""
event 对象最好单次使用，就是说，你创建一个 event 对象，让某个线程等待这个
对象，一旦这个对象被设置为真，你就应该丢弃它。尽管可以通过 clear() 方法来重
置 event 对象，但是很难确保安全地清理 event 对象并对它重新赋值。很可能会发生错
过事件、死锁或者其他问题（特别是，你无法保证重置 event 对象的代码会在线程再
次等待这个 event 对象之前执行）。如果一个线程需要不停地重复使用 event 对象，你
最好使用 Condition 对象来代替。下面的代码使用 Condition (对应CLinux里的条件变量)
对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到：
"""
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()  #创建一个条件对象

    def start(self):
        t = Thread(target=self.run())
        # 设置线程为后台线程,计时器线程
        t.daemon = True

        t.start()

    def run(self):
        while True:
            sleep(self._interval)   #睡眠后提醒所有线程
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()
                
def test02():
    #设置一个五秒的计时器,并开始执行
    ptimer = PeriodicTimer(5)
    ptimer.start()

    def count_down(nticks):
        while nticks:
            ptimer.wait_for_tick()
            print('T-minus', nticks)
            nticks += 1

    def countup(last):
        n = 0
        while n < last:
            ptimer.wait_for_tick()
            print('counting', n)
            n += 1

    Thread(target=count_down, args=(10,)).start()
    Thread(target=countup, args=(5,)).start()
    """
    event 对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程。如果你
    只想唤醒单个线程，最好是使用信号量或者 Condition 对象来替代。
    """

def worker(n, semaphore):
    # Wait to be signaled  等待被通知，所有线程都被阻塞在此处
    semaphore.acquire()
    # Do some work
    print('Working', n)

def test03():
    # Create some threads
    semaphore = Semaphore(0)
    n_workers = 10
    for n in range(n_workers):
        #循环创建进程，并指派worker任务
        t = Thread(target=worker, args=(n, semaphore))
        t.start()
    """
    编写涉及到大量的线程间同步问题的代码会让你痛不欲生。比较合适的方式是使用
    队列来进行线程间通信或者每个把线程当作一个 Actor，利用 Actor 模型来控制并发。
    """

if __name__ == '__main__':
    # test01()
    # test02()
    test03()
