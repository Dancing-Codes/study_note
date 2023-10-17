import re

class PathError(Exception):
    def __str__(self):
        return super().__str__()

def request_path(recv_info: str, method=2):
    #method 1:不用正则表达式提取
    if 1 == method:
        src_path, *_ = recv_info.split('\r')
        _, src_path, *_ = src_path.split(' ')
        return src_path

    #method 2: 正则表达式提取
    elif 2 == method:
        res = re.search('(/.*?\.(html|[a-z]+))+', recv_info)        
        if res:
            return res.group()
        else:
            raise PathError()

#测试用例
def main():
    test_info = 'POST /index/index.html http/1.1\r\nHost:localhost:8888\r\n'
    print(request_path(test_info))

if __name__ == '__main__':
    main()
    #测试通过^^
    