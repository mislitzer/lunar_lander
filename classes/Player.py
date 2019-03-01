class Player():
    def __init__(self, name, score = 0):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

