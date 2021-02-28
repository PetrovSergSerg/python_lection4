import model.utils as utils
from random import randint, getrandbits
import string

alphabet = string.ascii_letters


class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

    def set_empty_parameters(self):
        for name, value in self.__dict__.items():
            setattr(self, name, '')
        return self

    def set_random_parameters_to_random_value(self):
        if bool(getrandbits(1)):
            self.name = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.header = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        if bool(getrandbits(1)):
            self.footer = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        return self

    def set_all_parameters_to_random_value(self):
        self.name = utils.get_random_word(alphabet, randint(3, 10))
        self.header = utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.footer = utils.get_random_word(alphabet + ' ', randint(10, 20))
        return self
