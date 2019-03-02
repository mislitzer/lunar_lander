import arcade
from config import Constants as CONSTANTS

from random import randint

class Lunar():
    def __init__(self, x = 400, y = 400, delta_start_x = 0, delta_start_y = 0, radius = 8):
        self.__x = x
        self.__y = y
        self.__delta_x = delta_start_x
        self.__delta_y = delta_start_y
        self.__radius = radius
        self.__landing_pane_left = None
        self.__landing_pane_right = None
        self.__fuel = CONSTANTS.GAME_LUNAR_START_FUEL
        self.__landed = False
        self.__terminated = False

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

    @property
    def landing_pane_left(self):
        return self.__landing_pane_left

    @property
    def landing_pane_right(self):
        return self.__landing_pane_right

    @property
    def landed(self):
        return self.__landed

    @landed.setter
    def landed(self, value):
        self.__landed = value

    @property
    def fuel(self):
        if self.__fuel <= 0:
            return 0
        else:
            return self.__fuel

    @fuel.setter
    def fuel(self, value):
        self.__fuel = value
    
    @property
    def terminated(self):
        return self.__terminated

    @terminated.setter
    def terminated(self, value):
        self.__terminated = value
    
    @landing_pane_left.setter
    def landing_pane_left(self, value):
        self.__landing_pane_left = value

    @landing_pane_right.setter
    def landing_pane_right(self, value):
        self.__landing_pane_right = value

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
        self.landing_pane_left = ((self.x - self.radius * 2, self.y - 22), (self.x - self.radius, self.y - 22))
        self.landing_pane_right = ((self.x + self.radius * 2, self.y - 22), (self.x + self.radius, self.y - 22))

        arcade.draw_line(self.x - self.radius * 2, self.y - 22, self.x - self.radius, self.y - 22, arcade.color.WHITE, 5)
        arcade.draw_line(self.x + self.radius * 2, self.y - 22, self.x + self.radius, self.y - 22, arcade.color.WHITE, 5)

    def move_lunar_lander(self):
        self.x = self.x - self.delta_x
        self.y = self.y - self.delta_y

        if (self.landed == False):
            self.delta_y += CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT
        
        if (self.delta_x < 0.00):
            self.delta_x += CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT

        if (self.delta_x > 0.00):
            self.delta_x -= CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT

    def change_delta(self, key_control):
        if (key_control.key_up_pressed and self.fuel):
            self.delta_y -= CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT * CONSTANTS.GAME_LUNAR_VELOCITY
            self.fuel = self.fuel - CONSTANTS.GAME_LUNAR_FUEL_REDUCE
        
        if (key_control.key_right_pressed and self.fuel):
            self.delta_x -= CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT * CONSTANTS.GAME_LUNAR_VELOCITY
            self.fuel = self.fuel - (CONSTANTS.GAME_LUNAR_FUEL_REDUCE / CONSTANTS.GAME_LUNAR_FUEL_REDUCE_FACTOR)
        
        if (key_control.key_left_pressed and self.fuel):
            self.delta_x += CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT * CONSTANTS.GAME_LUNAR_VELOCITY
            self.fuel = self.fuel - (CONSTANTS.GAME_LUNAR_FUEL_REDUCE / CONSTANTS.GAME_LUNAR_FUEL_REDUCE_FACTOR)

        if self.y < 0:
            self.game_over()

    def game_over(self):
        self.terminated = True

    def check_line_collision(self, lines):
        for line in lines:
            start = line.shape.a
            end = line.shape.b

            line_tuple = ((start.x, start.y), (end.x, end.y))

            if (line.is_docker):
                pane_left_start_x = self.landing_pane_left[0][0]
                pane_left_start_y = self.landing_pane_left[0][1]
                pane_left_end_x = self.landing_pane_left[1][0]

                pane_right_start_x = self.landing_pane_right[0][0]
                pane_right_start_y = self.landing_pane_right[0][1]
                pane_right_end_x = self.landing_pane_right[1][0]
                
                if ((pane_left_end_x >= start.x and pane_right_start_x <= end.x) and (pane_left_start_y <= start.y or pane_right_start_y <= start.y)):
                    if (self.vertical_speed <= CONSTANTS.GAME_LUNAR_LANDING_TOLERANCE):
                        self.landed = True
                        self.delta_y = 0
                        
                        # increase by a fuel bonus
                        self.fuel += line.bonus

                        return line.score
                    else:
                        self.game_over()
                    
            
            if (arcade.geometry.are_polygons_intersecting(line_tuple, self.landing_pane_left)):
                self.game_over()
                return 0

            if (arcade.geometry.are_polygons_intersecting(line_tuple, self.landing_pane_right)):
                self.game_over()
                return 0

        return 0

    @property
    def horizontal_speed(self):
        delta_x_abs_factor = (self.delta_x * -1) * CONSTANTS.GAME_SPEED_FACTOR
        return int(delta_x_abs_factor)

    @property
    def vertical_speed(self):
        delta_y_abs_factor = self.delta_y * CONSTANTS.GAME_SPEED_FACTOR
        return int(delta_y_abs_factor)

    def set_lunar_to_start(self):
        width = CONSTANTS.GAME_WIDTH
        height = CONSTANTS.GAME_HEIGHT

        self.landed = False
        self.x = randint(int(width * 0.1), int(width - width * 0.1))
        self.y = height - height * 0.1
        self.delta_x = 0
        self.delta_y = 0