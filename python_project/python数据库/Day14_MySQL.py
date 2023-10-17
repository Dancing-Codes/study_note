import pymysql
import pyspark
from pyspark.sql import SparkSession


class Connector:
    def __init__(self, _user='root', _password='123456', _host='192.168.88.161', _database='db_1'):
        # 连接数据库，获取一个连接对象
        self._mysql = pymysql.Connect(user=_user, password=_password, host=_host, database=_database)
        # 获取一个查询游标
        # self._cursor = pymysql.cursors(self._mysql)

    # def query(self, sql: str):
    #     if isinstance(sql, str):
    #         return self._cursor.query('select * from bookinfo')
    #     else:
    #         raise Exception()

    def execute(self, sql: str):
        if isinstance(sql, str):
            return self._mysql.query(sql)
        else:
            raise ValueError()

    # def commit(self):
    #     self._cursor.commit()

    def close(self):
        # self._cursor.close()
        self._mysql.close()

    def isOpen(self):
        return self._mysql.open


def test(address='192.168.88.161', port=3306, protocol='mysql'):
    if protocol == 'mysql':
        try:
            mysql = pymysql.Connect(user='root', password='123456', host=address, database='hive3', port=port, charset='utf8')
        except Exception as e:
            print(e)
        else:
            s = mysql.query("select * from DBS")
            print(s)

def main():
    # c = Connector()
    # # if c.isOpen():
    # #     print('成功连接')
    # c.execute('select * from person')
    test()


if __name__ == '__main__':
    main()

