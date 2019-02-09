import pymunk
import arcade
import os

# import custom config
from config import Constants as CONSTANTS

# import custom classes
from classes import Level as level
from classes import Lunar as hallo

class LunarLander(arcade.Window):
    def __init__(self, width = CONSTANTS.GAME_WIDTH, height = CONSTANTS.GAME_HEIGHT):
        self.__gameboard = self.set_gameboard(super(), width, height)
        self.__level = level.Level(self.gameboard)
        self.__lunar = hallo.Lunar(width / 2, height - height * 0.1)
        self.__player = None

    def set_gameboard(self, parent, width, height):
        parent.__init__(width, height, CONSTANTS.GAME_TITLE)

        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        board = pymunk.Body(body_type=pymunk.Body.STATIC)

        return board

    def on_draw(self):
        arcade.start_render()

        for line in self.level.lines:
            start = line.shape.a
            end = line.shape.b
            thickness = line.thickness

            arcade.draw_line(start.x, start.y, end.x, end.y, arcade.color.WHITE, thickness)
        
        # draw the lunar lander
        self.lunar.draw_lunar_lander()
        # move the lunar lander for every game loop
        self.lunar.move_lunar_lander()

        # Figure out if the lunar lander hit the bottom and close
        if self.lunar.y < 0:
            arcade.close_window()



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

