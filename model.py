import datetime
from datetime import date
import socket
import pymysql.cursors
from conf_db import DATA
from connector_db import Connector
# Подключиться к базе данных.
class Model():
    connect = Connector()

    def set_Numbers (self, code, number, status):
        number_list =[(code),(number),(status)]

        connection = pymysql.connect(host=DATA['host'],
                                     user=DATA['user'],
                                     password=DATA['password'],
                                     db=DATA['db'],
                                     charset=DATA['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)

        insert_numbers_query = "INSERT INTO numbers_table (code, number, status) VALUES ( %s, %s, %s) "
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_numbers_query, number_list)
                connection.commit()
        finally:
            connection.close()

    # def update_numbers_date(self):

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
        insert_numbers_query = f"UPDATE numbers_table set status = 1  where id={id}"
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

    def update_numbers_date(self, id):
        a = date.today().isoformat()
        insert_numbers_query = f"UPDATE numbers_table SET date = {a} where id={id}"
        connection = pymysql.connect(host=DATA['host'],
                                     user=DATA['user'],
                                     password=DATA['password'],
                                     db=DATA['db'],
                                     charset=DATA['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_numbers_query)
                connection.commit()
        finally:
                connection.close()

    def get_last_update_number_id(self):
        record = ""
        a = date.today().isoformat()
        insert_numbers_query = f" select id from numbers_table where date is not null"
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
                record = cursor.fetchone()
                connection.commit()
                print("updated number")
        finally:
            connection.close()
        return record