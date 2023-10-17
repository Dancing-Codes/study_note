import os
from threading import Thread
"""
1、题目描述
使用进程实现文件夹的整体拷贝
在拷贝文件的文件时，如果文件夹中的文件很多，那么一个一个拷贝，效率会很低下
可以使用多任务的形式来实现文件夹下的文件进行同时拷贝。提高拷贝效率
"""

class DiractoryCopier:
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError
        try:
            with open(path, 'r') as f:
                str_info = f.read()
                file_list = str_info.split('\n')
                for val in file_list:
                    Thread(target=self.copy_task,args=(val,),daemon=True).start()
        except Exception as e:
            print(f'error happened, error infomation is {e}')
        
    def copy_task(self, file: str):
        with open(file,'rb') as f1:
            with open(f'{file}(1)', 'wb') as f2:
                f2.write(f1.read()) 
    
    @staticmethod
    def make(dirname:str='mydir'):  #在当前目录在创建目录，windows下的文件夹文件被系统遮挡，其他目录可能会出现 permisson denied
        if os.path.exists(f'./{dirname}'):
            return
        else:
            os.makedirs(f'./{dirname}')
            os.chdir(f'./{dirname}')
            with open('file1', 'w') as f:
                pass
            with open('file2', 'w') as f:
                pass
            with open('file3', 'w') as f:
                pass

#测试
def main():
    dirname = 'mydir'
    DiractoryCopier.make(dirname)
    DiractoryCopier(dirname)

if __name__ == '__main__':
    main()
# Permission denied，test failed