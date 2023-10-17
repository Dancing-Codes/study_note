from threading import Thread

class MyThread(Thread):
    def run(self) -> None:
        """
        重写Thread中的run方法
        :return:
        """
        print('这是我自己写的线程类')

if __name__ == '__main__':
    my_th = MyThread()
    my_th.start()