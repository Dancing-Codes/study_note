from threading import Thread
from random import randint
from time import time, sleep
"""
在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，
然而该模块过于底层，而且很多功能都没有提供，因此目前的多线程开发我们推荐使用
threading模块，该模块对多线程编程提供了更好的面向对象的封装。我们把刚才下载
文件的例子用多线程的方式来实现一遍
"""

def download(filename: str) -> None:
    print(f'{filename}正在下载...')
    sleep(randint(5, 10))
    print(f'{filename}下载完成')


def main():
    start = time()
    t1 = Thread(target=download, args=('python从入门到住院.pdf',))
    t2 = Thread(target=download, args=('Peking_Hot.avi',))
    #线程开始执行
    t1.start()
    t2.start()
    #阻塞等待线程退出
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗时{end - start}')


if __name__ == '__main__':
    main()
