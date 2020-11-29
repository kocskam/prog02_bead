class MissingDataException(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "Hiányzó adat: " + self.__value

class Player:

    def __init__(self, name, time):
        self.__name = name
        self.__time = time

    def getTime(self):
        return self.__time

    def getName(self):
        return self.__name

    def save2File(self, fout):
        print(self.__name + ";" + self.__time)