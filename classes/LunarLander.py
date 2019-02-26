import pymunk
import arcade
import os

from random import randint

# import custom config
from config import Constants as CONSTANTS

# import custom classes
from classes import Level as level
from classes import Lunar as hallo
from classes import KeyControl as control

class LunarLander(arcade.Window):
    def __init__(self, width = CONSTANTS.GAME_WIDTH, height = CONSTANTS.GAME_HEIGHT):
        self.__gameboard = self.set_gameboard(super(), width, height)
        self.__level = level.Level(self.gameboard)
        self.__lunar = hallo.Lunar(randint(int(width * 0.1), int(width - width * 0.1)), height - height * 0.1)
        self.__player = None
        self.__key_control = control.KeyControl()

    def set_gameboard(self, parent, width, height):
        parent.__init__(width, height, CONSTANTS.GAME_TITLE)

        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        board = pymunk.Body(body_type=pymunk.Body.STATIC)

        return board

    def on_draw(self):
        arcade.start_render()

        # change delta by key passing events
        self.lunar.change_delta(self.key_control)
        
        for line in self.level.lines:
            start = line.shape.a
            end = line.shape.b
            thickness = line.thickness
            
            # draw the lines and save it to the stack
            arcade.draw_line(start.x, start.y, end.x, end.y, arcade.color.WHITE, thickness)
        
        # draw the lunar lander
        self.lunar.draw_lunar_lander()
        # move the lunar lander for every game loop
        self.lunar.move_lunar_lander()
        self.lunar.check_line_collision(self.level.lines)

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

    @property
    def key_control(self):
        return self.__key_control

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_control.key_up_pressed = True
        elif key == arcade.key.RIGHT:
            self.key_control.key_right_pressed = True
        elif key == arcade.key.LEFT:
            self.key_control.key_left_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_control.key_up_pressed = False
        elif key == arcade.key.RIGHT:
            self.key_control.key_right_pressed = False
        elif key == arcade.key.LEFT:
            self.key_control.key_left_pressed = False

