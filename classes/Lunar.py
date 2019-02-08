import arcade
from config import Constants as CONSTANTS

class Lunar():
    def __init__(self, x = 400, y = 400, delta_start_x = 0, delta_start_y = 0, radius = 8):
        self.__x = x
        self.__y = y
        self.__delta_x = delta_start_x
        self.__delta_y = delta_start_y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def delta_x(self):
        return self.__delta_x

    @delta_x.setter
    def delta_x(self, value):
        self.__delta_x = value

    @property
    def delta_y(self):
        return self.__delta_y

    @delta_y.setter
    def delta_y(self, value):
        self.__delta_y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value
    
    def draw_lunar_lander(self):
        self.draw_lunar_lander_circle()
        self.draw_lunar_lander_rect()
        self.draw_lunar_lander_landing_legs()
        self.draw_lunar_lander_landing_panes()

    def draw_lunar_lander_circle(self):
        arcade.draw_circle_outline(self.x, self.y, self.radius, arcade.color.WHITE, 5)

    def draw_lunar_lander_rect(self):
        arcade.draw_rectangle_filled(self.x, self.y - self.radius, self.radius * 3, self.radius / 2, arcade.color.WHITE)

    def draw_lunar_lander_landing_legs(self):
        arcade.draw_line(self.x - self.radius / 1.5, self.y - self.radius, self.x - self.radius * 1.5, self.y - 22, arcade.color.WHITE, 5)
        arcade.draw_line(self.x + self.radius / 1.5, self.y - self.radius, self.x + self.radius * 1.5, self.y - 22, arcade.color.WHITE, 5)

    def draw_lunar_lander_landing_panes(self):
        arcade.draw_line(self.x - self.radius * 2, self.y - 22, self.x - self.radius, self.y - 22, arcade.color.WHITE, 5)
        arcade.draw_line(self.x + self.radius * 2, self.y - 22, self.x + self.radius, self.y - 22, arcade.color.WHITE, 5)

    def move_lunar_lander(self):
        self.x = self.x - self.delta_x
        self.y = self.y - self.delta_y

        self.delta_y += CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT