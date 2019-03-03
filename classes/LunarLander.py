import os
import time
from random import randint

import arcade
import pymunk

from classes import KeyControl as control
from classes import Level as level
from classes import Lunar as lunar
from classes import VocabularyMap as vcm
from classes import Player as player

from config import Constants as CONSTANTS


class LunarLander(arcade.Window):
    @property
    def gameboard(self):
        return self.__gameboard

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def lunar(self):
        return self.__lunar

    @lunar.setter
    def lunar(self, value):
        self.__lunar = value

    @property
    def player(self):
        return self.__player

    @property
    def key_control(self):
        return self.__key_control

    @property
    def player(self):
        return self.__player

    @property
    def has_level_overlay(self):
        return self.__has_level_overlay

    @has_level_overlay.setter
    def has_level_overlay(self, value):
        self.__has_level_overlay = value

    @property
    def started(self):
        return self.__started
    
    @property
    def vocab_map(self):
        return self.__vocab_map

    @started.setter
    def started(self, value):
        self.__started = value

    def __init__(self, width = CONSTANTS.GAME_WIDTH, height = CONSTANTS.GAME_HEIGHT):
        self.__gameboard = self.set_gameboard(super(), width, height)
        self.__level = level.Level(self.gameboard)
        self.__player = player.Player("")
        self.__lunar = self.set_lunar(width, height)
        self.__key_control = control.KeyControl()
        self.__has_level_overlay = False
        self.__started = False
        self.__vocab_map = vcm.VocabularyMap()

    def set_gameboard(self, parent, width, height):
        parent.__init__(width, height, CONSTANTS.GAME_TITLE)

        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        board = pymunk.Body(body_type=pymunk.Body.STATIC)

        return board

    def set_lunar(self, width, height):
        return lunar.Lunar(randint(int(width * 0.1), int(width - width * 0.1)), height - height * 0.1)

    def draw_background_scene(self):
        for star in self.level.stars:
            arcade.draw_circle_filled(star.x, star.y, star.radius, arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        # change delta by key passing events
        self.lunar.change_delta(self.key_control)

        self.draw_background_scene()
        
        for line in self.level.lines:
            start = line.shape.a
            end = line.shape.b
            thickness = line.thickness

            color = arcade.color.WHITE
            
            if line.is_docker:
                font_size = 14
                color = arcade.color.LIGHT_GREEN
                pos_y = start.y - font_size * 1.5

                if line.bonus:
                    arcade.draw_text("+" + str(line.bonus) + " fuel", start.x - ((start.x - end.x) / 10), start.y + font_size * 1.5, arcade.color.WHITE, font_size / 1.5)

                if (pos_y < 1):
                    if line.bonus:
                        arcade.draw_text("x" + str(line.score), start.x - ((start.x - end.x) / 2.6), start.y + font_size * 2.8, arcade.color.WHITE, font_size)
                    else:
                        arcade.draw_text("x" + str(line.score), start.x - ((start.x - end.x) / 2.6), start.y + font_size * 1.5, arcade.color.WHITE, font_size)
                else:
                    arcade.draw_text("x" + str(line.score), start.x - ((start.x - end.x) / 2.6), pos_y, arcade.color.WHITE, font_size)

            # draw the lines and save it to the stack
            arcade.draw_line(start.x, start.y, end.x, end.y, color, thickness)
        
        # draw the lunar lander
        self.lunar.draw_lunar_lander()

        if (self.lunar.landed == False and self.lunar.terminated == False and self.started):
            # move the lunar lander for every game loop
            self.lunar.move_lunar_lander()
            score = self.lunar.check_line_collision(self.level.lines)
            if (score > 0):
                self.player.score += score

        if (self.started == False):
            self.draw_level_overlay("PLEASE TYPE IN YOUR NAME", "and press ENTER to start", 22, 430, 225, 35)

        # draw info panel
        self.change_information_cycle()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_control.key_up_pressed = True
        elif key == arcade.key.RIGHT:
            self.key_control.key_right_pressed = True
        elif key == arcade.key.LEFT:
            self.key_control.key_left_pressed = True

        if key == arcade.key.ENTER and self.has_level_overlay and self.lunar.landed:
            self.close_level_overlay()
        elif key == arcade.key.ENTER and self.has_level_overlay and self.lunar.terminated:
            self.close_level_overlay(True)
            self.player.score = 0

        if (self.started == False):
            if key != arcade.key.ENTER and key != arcade.key.BACKSPACE:
                letter = self.vocab_map.get_vocab_of_key(key)
                if letter:
                    self.player.name += letter
                    self.draw_level_overlay("PLEASE TYPE IN YOUR NAME", "and press ENTER to start", 22, 430, 225, 35)
            elif key == arcade.key.ENTER:
                self.started = True
            elif key == arcade.key.BACKSPACE:
                shorted_name = self.player.name[:-1]
                self.player.name = shorted_name
                self.draw_level_overlay("PLEASE TYPE IN YOUR NAME", "and press ENTER to start", 22, 430, 225, 35)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.key_control.key_up_pressed = False
        elif key == arcade.key.RIGHT:
            self.key_control.key_right_pressed = False
        elif key == arcade.key.LEFT:
            self.key_control.key_left_pressed = False

    def draw_level_overlay(self, text, sub_text, font_size, width, sub_text_width, spacing = 0):
        self.has_level_overlay = True
        center_x = CONSTANTS.GAME_WIDTH / 2
        center_y = CONSTANTS.GAME_HEIGHT / 2
        rect_width = CONSTANTS.GAME_WIDTH / 1.5
        rect_height = CONSTANTS.GAME_HEIGHT / 5

        arcade.draw_rectangle_filled(center_x, center_y, rect_width, rect_height, arcade.color.BLACK)
        arcade.draw_rectangle_outline(center_x, center_y, rect_width, rect_height, arcade.color.WHITE, 2)
        arcade.draw_text(text, center_x - width / 2, center_y - (font_size / 2) + spacing, arcade.color.WHITE, font_size, width, None, None, True)

        if (sub_text):
            arcade.draw_text(sub_text, center_x - sub_text_width / 2, center_y - (font_size * 1.8) + spacing, arcade.color.WHITE, font_size / 1.5, sub_text_width)

        if (self.started == False):
            arcade.draw_text(self.player.name, center_x - width / 5, center_y - (font_size * 1.8) - (spacing / 2), arcade.color.WHITE, font_size, width, None, None, True)
        

    def change_information_cycle(self):
        start_x = 20
        start_y = CONSTANTS.GAME_HEIGHT - CONSTANTS.GAME_HEIGHT * 0.05
        font_size = 14
        line = font_size * 1.6
        
        name = self.player.name.upper()
        if self.started == False:
            name = ""

        arcade.draw_text(name, start_x, start_y, arcade.color.WHITE, font_size, 200, None, None, True)
        arcade.draw_text("LEVEL: " + str(int(self.level.handicap)), start_x, start_y - line * 2, arcade.color.WHITE, font_size, 200)
        arcade.draw_text("FUEL: " + str(int(self.lunar.fuel)), start_x, start_y - line * 3, arcade.color.WHITE, font_size, 200)

        if self.lunar.vertical_speed <= CONSTANTS.GAME_LUNAR_LANDING_TOLERANCE:
            arcade.draw_text("VERTICAL SPEED: " + str(self.lunar.vertical_speed), start_x, start_y - line * 4, arcade.color.LIGHT_GREEN, font_size, 200)
        else:
            arcade.draw_text("VERTICAL SPEED: " + str(self.lunar.vertical_speed), start_x, start_y - line * 4, arcade.color.RED, font_size, 200)

        arcade.draw_text("HORIZONTAL SPEED: " + str(self.lunar.horizontal_speed), start_x, start_y - line * 5, arcade.color.WHITE, font_size, 300)
        arcade.draw_text("SCORE: " + str(self.player.score), start_x, start_y - line * 6, arcade.color.WHITE, font_size, 300)

        if (self.lunar.landed):
            self.draw_level_overlay("LEVEL " + str(self.level.handicap) + " COMPLETED", "press ENTER to continue", 22, 320, 225)
        elif (self.lunar.terminated):
            self.draw_level_overlay("GAME OVER!", "press ENTER to restart", 22, 240, 225)

    def close_level_overlay(self, reset = False):
        self.has_level_overlay = False

        if (reset):
            self.lunar = self.set_lunar(CONSTANTS.GAME_WIDTH, CONSTANTS.GAME_HEIGHT)
            self.level = level.Level(self.gameboard)
            self.lunar.set_lunar_to_start()
        else:
            current_handicap = self.level.handicap
            self.level = level.Level(self.gameboard, current_handicap + 1)
            self.lunar.set_lunar_to_start()
