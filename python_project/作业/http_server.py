#避免重复造轮子!!!  ---python cookbook
from socketserver import TCPServer
from socket import socket

"""
题目：
实现代码，模拟实现服务器，获取通过浏览器客户端访问服务器的请求信息
并将请求报文进行分行显示
"""
class Http_Handle:
    def __init__(self, request: socket, client_address):
        try:
            request_info = str(request.recv(2048), encoding='utf-8')
        except Exception as e:
            print(f'recieve message failed, description: {e}')
        else:
            request_list_info = request_info.split('\r\n')
            for val in request_list_info:
                print(val)


def main():
    TCPServer(('',8080), Http_Handle)   #不需重复造轮子^^

if __name__ == '__main__':
    main()
    
