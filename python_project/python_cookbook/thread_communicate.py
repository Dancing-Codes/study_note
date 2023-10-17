from threading import Thread, Lock
from queue import Queue
from time import sleep
#线程间通讯
"""
从一个线程发送数据最安全的方式可能就是使用queue库中的队列了(进程也能如此)，创建一个被多个线程共享的Queue对象
这些线程通过使用put()和get()操作来向队列中添加或者删除元素，例如：
"""
#queue是线程安全的
def producer(out_q: Queue, mutex: Lock):
    n = 0
    #当队列的产品数量小于100时开始生产
    while True:
        if out_q.qsize() < 1000:
            mutex.acquire()
            n += 1
            out_q.put(n)
            print(f'生产了{n}')
            mutex.release()
        else:
            #等待消费
            sleep(0.1)

def consumer(in_q: Queue, mutex: Lock):
    while True:
        if in_q.qsize():
            mutex.acquire()
            print(f'消费了{in_q.get()}')
            mutex.release()
        else:
            #等待生产
            sleep(0.1)

def test01():
    q = Queue(1000)
    lock = Lock()
    Thread(args=(q, lock), target=producer).start()
    Thread(args=(q, lock), target=consumer).start()
    # Thread(args=(q, lock), target=consumer).start()
    #主线程在此等待子线程退出再退出

if __name__ == '__main__':
    test01()
