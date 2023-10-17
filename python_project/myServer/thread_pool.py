from threading import Thread, Lock, Timer
from time import sleep

class ThreadPool:
    _MAX_NUM_OF_THREADS = 10
    _ALIVE_THREAD_NUM = 0
    _THREADS_LIST_FLAG = []
    _RUNTIME_LEVEL = 1

    def __init__(self, num_threads=10):
        self._mutex = Lock()
        if num_threads != 10 and num_threads > 0:
            ThreadPool._MAX_NUM_OF_THREADS = num_threads

        self._mutex.acquire()
        manager_thread = Thread(target=self.manager_thread_task(), daemon=True)
        manager_thread.start()

        self._mutex.release()

    def manager_thread_task(self):
        while True:
            if ThreadPool._ALIVE_THREAD_NUM > ThreadPool._MAX_NUM_OF_THREADS:
                self._mutex.acquire()
                ThreadPool._THREADS_LIST_FLAG[0] = 0
                self._mutex.release()

    def __call__(self, *, task, client_socket, client_address_info):
        while True:
            if ThreadPool._ALIVE_THREAD_NUM < ThreadPool._MAX_NUM_OF_THREADS:
                self._mutex.acquire()
                ThreadPool._ALIVE_THREAD_NUM += 1
                Thread(target=task, args=(client_socket, client_address_info, ThreadPool._ALIVE_THREAD_NUM, ThreadPool.check)) \
                    .start()
                ThreadPool._THREADS_LIST_FLAG[ThreadPool._ALIVE_THREAD_NUM] = 1
                self._mutex.release()
            else:
                sleep(10)
                continue

    def __sizeof__(self):
        return ThreadPool._ALIVE_THREAD_NUM

    def __str__(self):
        return 'It\'s a thread pool'

    @classmethod
    def set_runtime_level(cls, level):
        ThreadPool._RUNTIME_LEVEL = level

    @classmethod
    def check(cls, flag) -> bool:
        return True if ThreadPool._THREADS_LIST_FLAG[flag] == 1 else False

