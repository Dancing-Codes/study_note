from codecs import decode, encode
# import threading
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET
from threading import Thread
from threading import Lock
from threading import Event
from time import sleep
from time import time
# from .clock import clock
import os


# 创建一个TCP服务器
class server:
    __mutex = Lock()
    __list_connected_client = []

    def __init__(self, addrfamily=AF_INET, socktype=SOCK_STREAM):
        # 创建socket对象
        self._sock = socket(family=addrfamily, type=socktype)
        # 设置端口复用
        self._sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        # 绑定本地IP地址和端口号，注意以元组形式传入
        self._sock.bind(('', 8888))
        # 监听端口,512代表连接队列大小
        self._sock.listen(512)
        # 循环接收连接请求
        while True:
            self.__list_connected_client.append(self._sock.accept())
            handle_thread = Thread(args=(self.__list_connected_client[len(self.__list_connected_client) - 1],),
                                   target=self.connection_handle)
            handle_thread.start()

    def manager_thread(self):
        manager = Thread(self.manager_job)
        manager.start()

    def manager_job(self):
        pass

    def connection_handle(self, tuple_client_info: tuple):
        client_sock: socket
        client_sock, client_addr = tuple_client_info
        msg = encode('\nHello ^_^, server connected!\n', encoding='gbk', errors='encode error')
        client_sock.send(msg)
        while True:
            send_menu(client_sock)
            # 从管道读，没有数据则阻塞等待
            msg = client_sock.recv(1024)
            msg = decode(msg, encoding='gbk', errors='decode error')
            msg = str(msg)
            if '1' == msg:
                client_sock.send(encode('该功能暂未提供，敬请期待...\n', encoding='gbk', errors='send error'))
                client_sock.send(encode('即将返回主菜单...\n', encoding='gbk', errors='send error'))
                sleep(3)
            elif '2' == msg:
                client_sock.send(encode('该功能暂未提供，敬请期待...', encoding='gbk', errors='send error'))
                client_sock.send(encode('即将返回主菜单...\n', encoding='gbk', errors='send error'))
                sleep(3)
            # elif '小花' == msg:
            # client_sock.send(encode(f'我喜欢你，{msg}\n', encoding='gbk', errors='send error'))
            # sleep(3)
            # continue
            elif '3' == msg:
                client_sock.send(encode('该功能暂未提供，敬请期待...', encoding='gbk', errors='send error'))
                client_sock.send(encode('即将返回主菜单...\n', encoding='gbk', errors='send error'))
                sleep(3)
            elif '4' == msg:
                client_sock.send(encode('该功能暂未提供，敬请期待...', encoding='gbk', errors='send error'))
                client_sock.send(encode('即将返回主菜单...\n', encoding='gbk', errors='send error'))
                sleep(3)
            elif '5' == msg:
                # 操作已连接列表，上锁
                self.__mutex.acquire()
                # 操作
                self.__list_connected_client.pop(self.__list_connected_client.index((client_sock, client_addr)))
                # 释放锁
                self.__mutex.release()
                client_sock.send(encode('数据保存成功，程序即将退出...', encoding='gbk', errors='send error'))
                sleep(3)
                client_sock.send(encode('感谢使用，再见~', encoding='gbk', errors='send error'))
                client_sock.close()
                break
            else:
                client_sock.send(encode('输入错误，请重新输入\n', encoding='gbk', errors='send error'))
                client_sock.send(encode('即将返回主菜单...\n', encoding='gbk', errors='send error'))
                sleep(3)
                continue


class send_menu:
    def __init__(self, client_sock: socket) -> None:
        client_sock.send(encode('*-' * 20 + '\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('1、查找学生\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('2、插入学生\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('3、删除学生\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('4、所有学生\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('5、退出系统\n', encoding='gbk', errors='menu error'))
        client_sock.send(encode('*-' * 20 + '\n', encoding='gbk', errors='menu error'))

class Printer:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass


def main():
    s = server()


if __name__ == '__main__':
    main()
