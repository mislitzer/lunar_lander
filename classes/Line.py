class Line():
    def __init__(self, shape, is_docker = False, score = 0, bonus = 0, thickness = 2):
        self.__shape = shape
        self.__is_docker = is_docker
        self.__score = score
        self.__bonus = bonus
        self.__thickness = thickness

    @property
    def shape(self):
        return self.__shape

    @property
    def is_docker(self):
        return self.__is_docker

    @property
    def score(self):
        return self.__score

    @property
    def bonus(self):
        return self.__bonus

    @property
    def thickness(self):
        return self.__thickness
