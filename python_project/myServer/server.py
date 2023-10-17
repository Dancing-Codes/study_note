from socket import socket, SOL_SOCKET, SOCK_STREAM, AF_INET, SO_REUSEADDR
from mysql_connector import MysqlConnector
from thread_pool import ThreadPool

class Server:
    """
    a log catch server
    """

    _mysql = MysqlConnector(username='root', password='123456')
    _thread_pool = ThreadPool()

    def __init__(self, _family=AF_INET, _type=SOCK_STREAM):
        self._sock = socket(_family, _type)
        self._sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        self._sock.bind(('node1', 12000))
        self._sock.listen(128)
        self.run()

    def run(self):
        while True:
            sock, client_address_info = self._sock.accept()
            Server._thread_pool(task=self.handle_task, client_socket=sock, client_address_info=client_address_info)

    def handle_task(self, *args):
        client_socket, client_address_info, alive_num, _check = args


