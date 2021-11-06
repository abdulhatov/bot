import pymysql.cursors
from conf_db import DATA
# Подключиться к базе данных.
class Model():

    def set_Numbers (self, code, number, status):
        number_list =[(code),(number),(status)]

        connection = pymysql.connect(host=DATA['host'],
                                     user=DATA['user'],
                                     password=DATA['password'],
                                     db=DATA['db'],
                                     charset=DATA['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")

        insert_numbers_query = "INSERT INTO numbers_table (code, number, status) VALUES ( %s, %s, %s) "
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_numbers_query, number_list)
                connection.commit()
        finally:
            # Закрыть соединение (Close connection).
            connection.close()

    def set_Date(name, date):
        date_list = [(name), (date)]

        connection = pymysql.connect(host=DATA['host'],
                                     user=DATA['user'],
                                     password=DATA['password'],
                                     db=DATA['db'],
                                     charset=DATA['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")
        insert_date_query = "INSERT INTO date_table (name, date) VALUES ( %s, %s) "
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_date_query, date_list)
                connection.commit()
            print("updated date")
        finally:
            # Закрыть соединение (Close connection).
            connection.close()


    def update_numbers(self, id):
        insert_numbers_query = f"UPDATE numbers_table set status = 1 where id={id}"
        connection = pymysql.connect(host=DATA['host'],
                                     user=DATA['user'],
                                     password=DATA['password'],
                                     db=DATA['db'],
                                     charset=DATA['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_numbers_query)
                connection.commit()
                print("updated number")
        finally:
                connection.close()

