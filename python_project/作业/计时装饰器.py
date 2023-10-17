from time import time 

# 实现装饰器，实现对函数执行时间进行计算的功能。
# 计时装饰器
def time_this(func):
    def inner(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        return end-start
    return inner

#测试用例
def main():
    @time_this
    def counter(num):
        while num:
            num -= 1
    return counter

if __name__ == '__main__':
    print(main()(10000))
    #测试通过^^    