import requests
import codecs
if __name__ == '__main__':
    _url = "https://www.baidu.com/img/bd_logo1.png"
    response = requests.get(_url)
    # print(response.text)  #出现大量中文乱码，解决如下
    # print(response.content) #二进制文件无法打印

    with open('D:/baidu.png', 'wb') as f:
        f.write(response.content)

