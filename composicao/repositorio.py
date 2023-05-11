from insert import Insert
from _select import Select

class Repository:
    def __init__(self):
        self.__select = Select()
        self.__insert = Insert()

    def insert_one(self):
        self.__insert.insert_one()

    def insert_many(self):
        self.__insert.insert_many()

    def select_many(self):
        self.__select.select_many()

    def select_one(self):
        self.__select.select_one()

