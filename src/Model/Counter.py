#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Counter:
    def __init__(self, middle_point, font, left_position):
        self.middle_point = middle_point
        self.font = font
        self.counter = 0
        self.at_left = left_position

    def draw(self, bg):
        msg = self.font.render(str(self.counter), True, (255, 255, 255))
        if self.at_left:
            text_w, text_h = msg.get_size()
            pos_x = self.middle_point - text_w - 10
        else:
            pos_x = self.middle_point + 5
        bg.blit(msg, (pos_x, 0))

    def add(self):
        self.counter += 1
