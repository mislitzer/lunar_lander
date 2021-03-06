import pymunk
import random
from classes import Line as line
from classes import Star as star
from config import Constants as CONSTANTS

class Level():
    def __init__(self, body, handicap = 1, gravity = (0.0, -900.0)):
        self.__body = body
        self.__space = pymunk.Space()
        self.__space.gravity = gravity
        self.__lines = []
        self.__docking_lines = []
        self.__handicap = handicap
        self.__gravity = gravity
        self.__stars = []

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
    def stars(self):
        return self.__stars

    @property
    def docking_lines(self):
        return self.__docking_lines

    def find_random_pos_line(self, points_amount):
        random_pos = random.randint(2, points_amount - 2)
        random_pos_up = random_pos + 1
        random_pos_down = random_pos - 1

        if (random_pos in self.docking_lines or random_pos_up in self.docking_lines or random_pos_down in self.docking_lines):
            self.find_random_pos_line(points_amount)
        elif (random_pos == None):
            self.find_random_pos_line(points_amount)
        else:
            return random_pos

    def generate_level(self):
        height_area = CONSTANTS.GAME_HEIGHT / 2
        points_amount = int(CONSTANTS.GAME_WIDTH / CONSTANTS.GAME_LINE_POINT_DISTRIBUTION) + 1
        docking_amount = 4

        # define the docking places
        for da in range(docking_amount):
            random_pos = self.find_random_pos_line(points_amount)
            if (random_pos):
                self.docking_lines.append(random_pos)

        # sort the places
        self.docking_lines.sort()
        
        # random selection of a bonus platform
        bonus_rand = random.randint(0, len(self.docking_lines) - 1)

        # positions
        start_position_x = 0
        position_y_start = None
        position_y_end = None
        docking_line_pointer = 0

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

                # multiply score twice
                if (len(self.docking_lines) < docking_amount):
                    score *= 2

                if docking_line_pointer == bonus_rand:
                    new_line = line.Line(shape, True, score, score * CONSTANTS.GAME_LUNAR_BONUS_FACTOR, 5)
                else:
                    new_line = line.Line(shape, True, score, 0, 5)

                docking_line_pointer += 1
            else:
                new_line = line.Line(shape)

            self.lines.append(new_line)

            start_position_x += CONSTANTS.GAME_LINE_POINT_DISTRIBUTION

        self.generate_background_stars()

    def generate_background_stars(self):
        amount_stars = CONSTANTS.GAME_BACKGROUND_STARS_AMOUNT
        game_width = CONSTANTS.GAME_WIDTH
        game_height = CONSTANTS.GAME_HEIGHT

        for s in range(amount_stars):
            rand_x = random.randint(1, game_width - 1)
            rand_y = random.randint(1, game_height - 1)
            rand_radius_multiplier = random.randint(1, 3)
            radius = CONSTANTS.GAME_BACKGROUND_STARS_BASE_RADIUS * rand_radius_multiplier

            generated_star = star.Star(rand_x, rand_y, radius)
        
            self.stars.append(generated_star)

