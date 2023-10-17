from pymysql import Connect

class MysqlConnector:
    def __init__(self, *, username, password, host='node1', port=3306):
        try:
            self._mc = Connect(user=username, password=password, host=host, port=port, charset='utf8')
        except Exception as e:
            pass
        self._cs = self._mc.cursor()

