#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Bar:
    def __init__(self, initial_x, initial_y):
        self.pos_x = initial_x
        self.pos_y = initial_y
        self.vy = 0

    def update(self):
        self.pos_y += self.vy

    def get_y(self):
        return self.pos_y

    def set_y(self, y):
        self.pos_y = y

    def set_vy(self, vy):
        self.vy = vy

    def get_x(self):
        return self.pos_x

    def draw(self, bg):
        pygame.draw.rect(bg, (255, 255, 255), (self.pos_x, self.pos_y, 5, 50))
