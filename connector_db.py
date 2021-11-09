
import pymysql.cursors
from conf_db import DATA

class Connector():
    def connection(self):
        connection = pymysql.connect(host=DATA['host'],
                                             user=DATA['user'],
                                             password=DATA['password'],
                                             db=DATA['db'],
                                             charset=DATA['charset'],
                                    cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")
        return connection