from multiprocessing.context import Process
from os import getpid
from time import sleep  #, time
# from queue import Queue     #消息队列
"""
我们启动两个线程，一个输出Ping，一个输出Pong，两个进程输出的结果加起来一共十个
"""
counter = 0
def print_task(content: str) -> None:
    global counter
    while counter < 10:
        print(f'进程{getpid()}打印{content},counter={counter}')
        counter += 1
        sleep(0.01)

def main():
    #创建进程对象，此时进程并未创建
    proc1 = Process(target=print_task, args=('ping',))
    proc2 = Process(target=print_task, args=('pong',))
    #开启两个进程，进程被创建并执行相应的任务函数
    proc1.start()
    proc2.start()

    #阻塞，等待进程退出，释放资源
    proc1.join()
    proc2.join()

#------------------------------------------------------------------
#消息队列
# Queue
# 使用对列完成对进程间的通讯


if __name__ == '__main__':
    main()
#程序输出结果如下
'''
进程8372打印ping,counter=0
进程4448打印pong,counter=0
进程4448打印pong,counter=1
进程8372打印ping,counter=1
进程8372打印ping,counter=2
进程4448打印pong,counter=2
进程8372打印ping,counter=3进程4448打印pong,counter=3

进程8372打印ping,counter=4
进程4448打印pong,counter=4
进程4448打印pong,counter=5
进程8372打印ping,counter=5
进程8372打印ping,counter=6
进程4448打印pong,counter=6
进程8372打印ping,counter=7进程4448打印pong,counter=7

进程8372打印ping,counter=8
进程4448打印pong,counter=8
进程8372打印ping,counter=9
进程4448打印pong,counter=9

'''
"""
结果分析：
1、ping,pong各自输出了十个？
当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，
每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个
counter变量，所以结果也就可想而知了
2、打印的格式紊乱、不整齐？
进程1中的print函数还没执行完，CPU时间片就被进程2抢走，两个进程交替执行
另外，也说明了print函数不是原子的，也不是线程安全的
------------------------------------------------------------
要解决这些问题比较简单的办法是使用multiprocessing模块中的Queue类，它是可以被
多个进程共享的队列，底层是通过管道和信号量（semaphore）机制来实现的
"""
