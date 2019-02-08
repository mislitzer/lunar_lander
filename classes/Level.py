import pymunk
import random
from classes import Line as line
from config import Constants as CONSTANTS

class Level():
    def __init__(self, body, handicap = 0, gravity = (0.0, -900.0)):
        self.__body = body
        self.__space = pymunk.Space()
        self.__space.gravity = gravity
        self.__lines = []
        self.__docking_lines = []
        self.__handicap = handicap
        self.__gravity = gravity

        # draw the level
        self.generate_level()

    @property
    def body(self):
        return self.__body

    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, value):
        self.__space = value

    def add_to_level_space(self, value):
        self.__space.add(self.body, value)

    @property
    def handicap(self):
        return self.__handicap

    @handicap.setter
    def handicap(self, value):
        self.__handicap = value

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, value):
        self.__gravity = value

    @property
    def lines(self):
        return self.__lines

    @property
    def docking_lines(self):
        return self.__docking_lines

    def generate_level(self):
        height_area = CONSTANTS.GAME_HEIGHT / 2
        points_amount = int(CONSTANTS.GAME_WIDTH / CONSTANTS.GAME_LINE_POINT_DISTRIBUTION) + 1
        docking_amount = 4

        # define the docking places
        for da in range(docking_amount):
            random_pos = random.randint(1, points_amount - 1)
            self.docking_lines.append(random_pos)

        # sort the places
        self.docking_lines.sort()

        # positions
        start_position_x = 0
        position_y_start = None
        position_y_end = None

        for p in range(points_amount):
            is_docking_line = False

            if (position_y_end):
                position_y_start = position_y_end
            else:
                position_y_start = random.randint(0, height_area)

            position_y_end = random.randint(0, height_area)

            # check for even track point
            if (p in self.docking_lines):
                position_y_end = position_y_start
                is_docking_line = True

            shape = pymunk.Segment(self.body, [start_position_x, position_y_start], [start_position_x + CONSTANTS.GAME_LINE_POINT_DISTRIBUTION, position_y_end], 0.0)
            shape.friction = CONSTANTS.GAME_SHAPE_FRICTION

            if (is_docking_line):
                rand_score = random.randint(0, 1)
                if (rand_score == 1):
                    score = 4
                else:
                    score = 2

                new_line = line.Line(shape, True, score, 5)
            else:
                new_line = line.Line(shape)

            self.lines.append(new_line)

            start_position_x += CONSTANTS.GAME_LINE_POINT_DISTRIBUTION
