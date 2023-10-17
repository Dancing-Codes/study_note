from codecs import decode
from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from random import randint
from time import sleep

class Server_ChatRobot:
    
    __connected_list = []

    _poem_list = ['东临碣石，以观沧海', '山重水复疑无路，柳暗花明又一村', '我寄愁心与明月，随风直到夜郎西', '君子见机，达人知命',
                     '落霞与孤鹜齐飞，秋水共长天一色', '宝剑锋从磨砺出，梅花香自苦寒来', '瀚海阑干百丈冰，愁云惨淡万里凝',
                     '山回路转不见君，雪上空留马行处', '春江潮水连海平，海上明月共潮生', '大漠孤烟直，长河落日圆',
                     '春花秋月何时了，往事知多少', '枯藤老树昏鸦，小桥流水人家', '沉舟侧畔千帆过，病树前头万木春',
                     '衣带渐宽终不悔，为伊消得人憔悴', '黄金百战穿金甲，不断楼兰誓不还', '生当作人杰，死亦为鬼雄',
                     '残雪凝晖冷画屏，落梅横笛已三更', '我是人间惆怅客，知君何事泪纵横', '寻寻觅觅，冷冷清清',
                     '红藕香残玉簟秋，轻解罗裳，独上兰舟']

    _send_list = ['收到你的内容，我想说的是:', '送你一句话:', '你认识这句古诗吗？', '^_^:', '这句诗符合你的心意吗？']

    _msg_recv = []

    def __init__(self, addr_family=AF_INET,_type=SOCK_STREAM) -> None:
        self._server_sock = socket(addr_family, _type)
        self._server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        self._server_sock.bind(('', 8080))
        self._server_sock.listen(128)

        while True:
            self.__connected_list.append(self._server_sock.accept())
            Thread(args=(self.__connected_list[len(self.__connected_list)-1],), target=self.access_handle).start()


    def access_handle(self, client_info: tuple) -> None:
        client_socket: socket
        client_socket, client_addr_port = client_info
        client_socket.send(bytes('\n我：打个招呼，你好~\n', encoding='gbk'))
        while True:
            # try:
            msg = decode(client_socket.recv(1024), encoding='gbk', errors='decode error')
            # except Exception:
                # break

            if msg:
                self._msg_recv.append(msg)
                if msg == 'bye' or msg.find('退出')+1 or msg.find('不玩了')+1:
                    client_socket.send(bytes(f'你：{msg}', encoding='gbk'))
                    break
                client_socket.send(bytes(f'你：{msg}', encoding='gbk'))
                sleep(0.5)
                client_socket.send(bytes(f'\n我：{self._send_list[randint(0,len(self._send_list)-1)]}\n    {self._poem_list[randint(0,len(self._poem_list))]}\n', encoding='gbk'))
                continue

            else:
                client_socket.send(bytes(f'我：想要退出了吗？\n', encoding='gbk'))
                try:
                    msg = client_socket.recv(1024)
                except Exception:
                    client_socket.close
                    self.__connected_list.pop(self.__connected_list.index((client_socket,client_addr_port)))
                    return
                if not msg:
                    break
                elif str(msg) == 'bye':
                    break
                else:
                    msg = str(msg)
                    if msg.find('嗯')+1 or msg.find('是的')+1 or msg.find('好')+1 or msg.find('ok')+1 or msg.find('yes')+1 or msg.find('bye')+1:
                        client_socket.send(bytes(f'我：就要退出了了呢，最后我想说:\n{self._poem_list[randint(0,len(self._poem_list))]}\n', encoding='gbk'))
                        sleep(3)
                        client_socket.send(bytes('bye~\n', encoding='gbk'))
                        client_socket.close()
                        self._poem_list.pop(self._poem_list.index((client_socket,client_addr_port)))
                        return

        client_socket.send(bytes(f'我：就要退出了了呢，最后我想说:\n{self._poem_list[randint(0,len(self._poem_list)-1)]}\n', encoding='gbk'))
        sleep(3)
        client_socket.send(bytes('bye~\n', encoding='gbk'))
        client_socket.close()
        self.__connected_list.pop(self.__connected_list.index((client_socket,client_addr_port)))
        return
        

def main():
    Server_ChatRobot()

if __name__ == '__main__':
    main()
    
                
