#python中的多进程
from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid, kill
"""
Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，
创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。fork()函数非
常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，而子进程中的
返回值永远都是0。Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，
因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，
而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列
（Queue）和管道（Pipe）等。
"""

def download_task(filename: str) -> None:
    print(f'开始下载{filename}...')
    time_to_download = randint(5, 10)
    sleep(time_to_download)     #系统睡眠
    print(f'下载{filename}完成，耗费了{time_to_download}秒')
    kill(getpid(), 9)

def main():
    start = time()
    download_task('python从入门到住院.pdf')
    download_task('Peking_Hot.avi')
    end = time()
    print(f'总共耗费了{end - start}')

# if __name__ == '__main__':
#     main()            #耗费了14秒

#从以上例子可以看出，如果程序只能一步步往下执行，那么即使两个毫不相关的下载任务，也
#需要先等待一个文件下载完，然后再开始下载另外一个文件，这不合理也不是我们想看到的
'我们尝试将任务放到不同进程中进行优化'
def multi_download(filename: str) -> None:
    print(f'进程{getpid()}开始下载{filename}...')
    download_time = randint(5, 10)
    sleep(download_time)
    print(f'{getpid()}进程已经下载完{filename},耗时{download_time}')

def multi_main():
    start = time()
    proc1 = Process(target=multi_download, args=('Python从入门到住院',))
    proc1.start()
    proc2 = Process(target=multi_download, args=('Peking_Hot.avi',))
    proc2.start()
    proc1.join()
    proc2.join()
    end = time()
    print(f'总共花费了{end - start}秒')

if __name__ == '__main__':
    multi_main()    #耗费了9秒
'''
在上面的代码中，我们通过Process类创建了进程对象，通过target参数我们传入
一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给
函数的参数。Process对象的start方法用来启动进程，而join方法表示等待进程执
行结束。运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时
间将大大缩短，不再是两个任务的时间总和。下面是程序的一次执行结果。
'''
"""
进程9984开始下载Python从入门到住院...
进程3140开始下载Peking_Hot.avi...
3140进程已经下载完Peking_Hot.avi,耗时5
9984进程已经下载完Python从入门到住院,耗时9
总共花费了9.156330585479736秒
"""
#我们也可以使用subprocess模块中的类和函数来创建和启动子进程，然后通过管道来和子进程通信