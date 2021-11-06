import pymysql.cursors
from conf_db import DATA

class ChekData():
    def get_number_id(self, id):
        record = 0
        try:
            connection = pymysql.connect(host=DATA['host'],
                                         user=DATA['user'],
                                         password=DATA['password'],
                                         db=DATA['db'],
                                         charset=DATA['charset'],
                                         cursorclass=pymysql.cursors.DictCursor)

            cursor = connection.cursor()
            sql_select_query = """select number from numbers_table where id = %s"""
            # set variable in query
            cursor.execute(sql_select_query, (id))
            # fetch result
            record = cursor.fetchone()

        except:
            print("Failed to get record from MySQL table")
        finally:
            if connection.connect():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return record

    def get_range(self):
        max_id = 0
        try:
            connection = pymysql.connect(host=DATA['host'],
                                         user=DATA['user'],
                                         password=DATA['password'],
                                         db=DATA['db'],
                                         charset=DATA['charset'],
                                         cursorclass=pymysql.cursors.DictCursor)

            cursor = connection.cursor()
            sql_select_query = """select max(id) from numbers_table"""
            # set variable in query
            cursor.execute(sql_select_query)
            # fetch result
            max_id = cursor.fetchone()

        except:
            print("Failed to get record from MySQL table")
        finally:
            if connection.connect():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return max_id
