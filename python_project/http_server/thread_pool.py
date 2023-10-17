# from os import terminal_size
from threading import Thread
from threading import Lock


class ThreadPool:
        
    def __init__(self, task=None, max_thread_num: int = 10) -> None:
        if task:
            self.__task = task
        
        self._max_thread_num = max_thread_num
        self._thread_live_num = 0
        self._thread = []
        self.__mutex = Lock()
        
        Thread(target=self.manager_task, daemon=True).start()

    def thread_run(self, task, args) -> None:
        """
        this function will create a thread and run
        the task that user given, the parameter args
        is a HTTP GET path
        return None
        """
        if task:
            self.__task = task
        
        t = Thread(target=self.__task, args=args, daemon=True)
        self.__mutex.acquire()
        t.start()
        for i, val in enumerate(self._thread):
            if val is None:
                self._thread[i] = t
                break
        else:
            self._thread.append(t)
        self._thread_live_num += 1
        self.__mutex.release()
        return

    def manager_task(self):
        thread: Thread
        while True:
            for index, thread in enumerate(self._thread):
                if not thread.is_alive():
                    self.__mutex.acquire()
                    self._thread.pop(index)
                    self._thread_live_num -= 1
                    self.__mutex.release()
            if self._thread_live_num > self._max_thread_num:
                self.__mutex.acquire()
                print('超过最大线程数限制，注意系统资源消耗')
                self.__mutex.release()
    
    def __str__(self) -> str:
        return f'线程池，包括管理者线程一共{self._thread_live_num+1}个线程'
    
    def __sizeof__(self) -> int:
        return self._thread_live_num+1


if __name__ == '__main__':
    # main()
    pass