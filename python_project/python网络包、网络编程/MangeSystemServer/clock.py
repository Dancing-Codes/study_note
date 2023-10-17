from time import time
from threading import Event, Thread


class clock:

    #初始化一个时钟进程，负责后台计时，有超时事件发送，立刻通知event
    def __init__(self, ev: Event) -> None:
        self.t = Thread(target=self.run_clock, args=(ev,))
        self.t.start()
        self.t.daemon = True

    def run_clock(self, ev: Event):
        start_time = time()

        #当开始时间和现在时间相差30秒以内时，保持轮询
        while (start_time - time()) < 30:
            continue

        #否则,发出事件提醒
        ev.set()
        
        #闹钟线程结束
        

