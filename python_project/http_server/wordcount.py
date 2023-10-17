from mrjob.job import MRJob

class WordCount(MRJob):

    def __init__(self, *args, **kwargs):
        super(WordCount, self).__init__(*args, **kwargs)
        self.chars = 0
        self.words = 0

    def mapper(self, _, line):  #不关心文件偏移量，根据空格对文本进行切分
        self.chars += len(line) + 1
        self.words += sum(1 for word in line.split(' ') if word.strip())

    def reducer(self, key, values):
        #生成可迭代对象返回
        yield key, sum(values)


if __name__ == '__main__':
    WordCount.run()