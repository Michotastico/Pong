#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Ball:
    def __init__(self, initial_x, initial_y, vx, vy):
        self.pos_x = initial_x
        self.pos_y = initial_y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.pos_x += self.vx
        self.pos_y += self.vy

    def draw(self, bg):
        pygame.draw.rect(bg, (255, 255, 255), (self.pos_x, self.pos_y, 10, 10))

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy
