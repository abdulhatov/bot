import datetime

from view import View
from chek_data import ChekData
from model import *
def main():
    view = View()
    model = Model()
    checkData = ChekData()
    if checkData.get_number_id(1):
       view.getData()
    else:
        view.full_up_database()
    view.getData()
#
if __name__ == "__main__":
    main()