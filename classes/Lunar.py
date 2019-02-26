import arcade
from config import Constants as CONSTANTS

class Lunar():
    def __init__(self, x = 400, y = 400, delta_start_x = 0, delta_start_y = 0, radius = 8):
        self.__x = x
        self.__y = y
        self.__delta_x = delta_start_x
        self.__delta_y = delta_start_y
        self.__radius = radius
        self.__landing_pane_left = None
        self.__landing_pane_right = None

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

        self.delta_y += CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT

    def change_delta(self, key_control):
        if (key_control.key_up_pressed):
            self.delta_y -= CONSTANTS.GAME_LUNAR_GRAVITY_CONSTANT * CONSTANTS.GAME_LUNAR_VELOCITY

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
                    print("IS ON DOCKKKKKKERR :)")
                    print(line.score)
            
            if (arcade.geometry.are_polygons_intersecting(line_tuple, self.landing_pane_left)):
                print("collision detected LEFT")
                print(line.score)

            if (arcade.geometry.are_polygons_intersecting(line_tuple, self.landing_pane_right)):
                print("collision detected RIGHT")
                print(line.score)

        