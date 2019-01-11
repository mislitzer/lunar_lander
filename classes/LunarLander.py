import pymunk
import arcade
import os

# import custom config
from config import Constants as CONSTANTS

# import custom classes
from classes import Level as level
from classes import Lunar as lunar

class LunarLander(arcade.Window):
    def __init__(self, width = CONSTANTS.GAME_WIDTH, height = CONSTANTS.GAME_HEIGHT):
        # set the gameboard
        self.__gameboard = self.set_gameboard(super(), width, height)
        self.__level = level.Level(self.gameboard)
        self.__lunar = lunar.Lunar()
        self.__player = None

        self.level.add_to_level_space(self.lunar.shape)

    def set_gameboard(self, parent, width, height):
        parent.__init__(width, height, CONSTANTS.GAME_TITLE)

        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        board = pymunk.Body(body_type=pymunk.Body.STATIC)

        return board

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_outline(CONSTANTS.GAME_WIDTH / 2, CONSTANTS.GAME_HEIGHT - 20, self.lunar.shape.radius, arcade.color.WHITE, 2)

        for line in self.level.lines:
            start = line.shape.a
            end = line.shape.b
            thickness = line.thickness

            arcade.draw_line(start.x, start.y, end.x, end.y, arcade.color.WHITE, thickness)

    def update(self, delta_time):

        self.lunar.body.center_x = 50
        self.lunar.body.center_y = 50
        # ball.angle = math.degrees(ball.pymunk_shape.body.angle)

        

    @property
    def gameboard(self):
        return self.__gameboard

    @property
    def level(self):
        return self.__level

    @property
    def lunar(self):
        return self.__lunar

    @property
    def player(self):
        return self.__player

