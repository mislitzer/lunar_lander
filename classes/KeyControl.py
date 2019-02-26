import arcade

class KeyControl(arcade.Window):
    def __init__(self):
        self.__key_up_pressed = False
        self.__key_right_pressed = False
        self.__key_down_pressed = False
        self.__key_left_pressed = False

    @property
    def key_up_pressed(self):
        return self.__key_up_pressed

    @property
    def key_right_pressed(self):
        return self.__key_right_pressed

    @property
    def key_down_pressed(self):
        return self.__key_down_pressed

    @property
    def key_left_pressed(self):
        return self.__key_left_pressed
    
    @key_up_pressed.setter
    def key_up_pressed(self, value):
        self.__key_up_pressed = value

    @key_right_pressed.setter
    def key_right_pressed(self, value):
        self.__key_right_pressed = value

    @key_down_pressed.setter
    def key_down_pressed(self, value):
        self.__key_down_pressed = value

    @key_left_pressed.setter
    def key_left_pressed(self, value):
        self.__key_left_pressed = value