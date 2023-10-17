from socket import socket, SOL_SOCKET, SO_REUSEADDR, AF_INET, SOCK_STREAM
from codecs import decode, encode
import thread_pool


class HttpServer:

    def __init__(self, _family=AF_INET, _type=SOCK_STREAM, port=9090) -> None:

        # 1、服务器初始化，基于TCP/IP协议
        self._server_sock = socket(family=_family, type=_type)
        # 2、设置端口口复用
        self._server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        # 3、绑定
        self._server_sock.bind(('', port))
        # 4、监听
        self._server_sock.listen(128)

        # 创建线程池对象
        self.__t_pool = thread_pool.ThreadPool()
        self.server_run()

    def server_run(self):
        # 循环等待客户端连接
        while True:
            # 接收客户端连接
            try:
                self.__t_pool.thread_run(self.http_task, self._server_sock.accept())
            except Exception as e:
                print('thread_run error', e)

    def http_task(self, *args):
        client_socket, client_info = args
        print(f'来自客户端的连接：{client_info}')

        # 接收游览器的请求报文
        recv_data = client_socket.recv(1024)
        if len(recv_data) == 0:
            print(f'客户端下线')
            client_socket.close()
            return

        str_info = decode(recv_data, encoding='utf-8')
        print(str_info)

        # 分割请求报文
        _, recv_path, *_ = str_info.split(' ')

        if recv_path == '/':
            try:
                with open(f'static\\index.html', 'rb') as f:
                    file_data = f.read()
            except Exception as e:
                # 构建响应报文并返回
                # 响应行
                response_line = 'HTTP/1.1 404 PERMISSION DENY\r\n'
                # 响应头
                response_head = 'Server: NB/1.0\r\n\r\n'
                # 响应体
                with open(f'static\\error.html', 'rb') as ferror:
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + ferror.read())
            else:
                # 构建响应报文并返回
                # 响应行
                response_line = 'HTTP/1.1 200 OK\r\n'
                # 响应头
                response_head = 'Server: NB/1.0\r\n\r\n'
                # 响应体
                client_socket.send(encode(response_line + response_head, encoding='utf-8') + file_data)

        elif recv_path == '/check_student':
            try:
                with open(f'static\\{recv_path[0:]}.html', 'rb') as f:
                    # 响应行
                    response_line = 'HTTP/1.1 200 OK\r\n'
                    # 响应头
                    response_head = 'Server: NB/1.0\r\n\r\n'
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + f.read())
            except Exception as e:
                # 构建响应报文并返回
                # 响应行
                response_line = 'HTTP/1.1 404 PERMISS DENY\r\n'
                # 响应头
                response_head = 'Server: NB/1.0\r\n\r\n'
                # 响应体
                with open(f'static\\error.html', 'rb') as ferror:
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + ferror.read())

        elif recv_path == '/delete_student':
            try:
                with open(f'static\\{recv_path[1:]}.html', 'rb') as f:
                    # 响应行
                    response_line = 'HTTP/1.1 200 OK\r\n'
                    # 响应头
                    response_head = 'Server: NB/1.0\r\n\r\n'
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + f.read())
            except Exception as e:
                # 构建响应报文并返回
                # 响应行
                response_line = 'HTTP/1.1 404 PERMISSION DENY\r\n'
                # 响应头
                response_head = 'Server: NB/1.0\r\n\r\n'
                # 响应体
                with open(f'static\\error.html', 'rb') as ferror:
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + ferror.read())

        elif recv_path == '/insert_student':
            try:
                with open(f'static\\{recv_path[1:]}.html', 'rb') as f:
                    # 响应行
                    response_line = 'HTTP/1.1 200 OK\r\n'
                    # 响应头
                    response_head = 'Server: NB/1.0\r\n\r\n'
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + f.read())
            except Exception as e:
                # 构建响应报文并返回
                # 响应行
                response_line = 'HTTP/1.1 404 PERMISSION DENY\r\n'
                # 响应头
                response_head = 'Server: NB/1.0\r\n\r\n'
                # 响应体
                with open(f'static\\error.html', 'rb') as ferror:
                    client_socket.send(encode(response_line + response_head, encoding='utf-8') + ferror.read())

        client_socket.close()


if __name__ == '__main__':
    pass
