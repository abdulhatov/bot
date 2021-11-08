import time
import socket
from datetime import date
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from  model import Model
from chek_data import ChekData
class View():

    def __init__(self):
        self.model = Model
        self.checkdb = ChekData
        self.code = 500
        self.numbers = 1
        self.status = 0
        self.code_list = [500, 509, 550, 559, 700, 709, 755, 756, 990, 999, 0]
        self.index = 1
        self.n = 0

    def getData(self):
        self.driver = webdriver.Chrome()
        while True:
            self.loop(self.code)
            if self.code == 999:
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)
                today = date.today()
                self.model.set_Date(local_ip, today)
                break

            self.code = self.code + 1

            if self.code == self.code_list[self.index] + 1:
                self.index = self.index + 1
                self.code = self.code_list[self.index]
                self.index = self.index + 1

    def loop(self, code):
        to = self.checkdb.get_range(self)
        for i in range(1, int(to['max(id)'])):

            n = int(f'996{self.code}''{:>06d}'.format(((self.checkdb.get_number_id(ChekData,i)['number']))))
            self.driver.get(f"https://web.whatsapp.com/send?phone={n}")
            time.sleep(8)

            s = "Tap Menu\nor Settings\nand select Linked Devices"
            if (self.driver.find_element(By.CLASS_NAME, value="i0jNr").text) == s:
                self.driver.close()
                break

            else:
                try:
                    elem = self.driver.find_element(By.CLASS_NAME, value="_2Nr6U")
                    print("This number don't used whatsapp!")
                except NoSuchElementException:
                    print("This number use whatsapp!")
                    self.model.update_numbers(Model, i)

    def full_up_database(self):
        print("Database is fulling up.....")
        print("This take a some time!")
        while True:

            for number in range(0, 1000000):
                self.model.set_Numbers(Model, self.code, number, status=0)

            if self.code == 999:
                break

            self.code = self.code + 1

            if self.code == self.code_list[self.index] + 1:
                self.index = self.index + 1
                self.code = self.code_list[self.index]
                self.index = self.index + 1

        print("Database has been ful up")