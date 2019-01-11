import pymunk
import arcade

class Lunar():

    def __init__(self):
        x = 100
        y = 100

        self.__body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.__body.position = x, y
        self.__shape = pymunk.Circle(self.__body, 10)
        self.__shape.friction = 0.3

        # self.space.add(body, shape)

    @property
    def body(self):
        return self.__body

    @property
    def shape(self):
        return self.__shape
