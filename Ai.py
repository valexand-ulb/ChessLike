from copy import deepcopy
from random import shuffle


class Ai:
    def __init__(self, index, parent, deep=2):
        self.index = index
        if self.index == 1:
            self.color = 'red'
            self.corner = 'ul'
        elif self.index == 2:
            self.color = 'green'
            self.corner = 'ur'
        elif self.index == 3:
            self.color = 'blue'
            self.corner = 'dr'
        else:
            self.color = 'yellow'
            self.corner = 'dl'

        self.parent = parent
        self.i = deep

    def play(self, mat):
        self.minimax(mat, self.index)
