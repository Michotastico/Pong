#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Window:
    def __init__(self, screen, bar_1, bar_2, ball, counter_1, counter_2):
        self.bg = screen
        self.color = (0, 0, 0)
        self.bar_one = bar_1
        self.bar_two = bar_2
        self.ball = ball
        self.counter_one = counter_1
        self.counter_two = counter_2
        self.width, self.height = self.bg.get_size()

    def clean(self):
        self.bg.fill(self.color)

    def draw(self):
        self.bar_one.draw(self.bg)
        self.bar_two.draw(self.bg)
        self.ball.draw(self.bg)
        self.counter_one.draw(self.bg)
        self.counter_two.draw(self.bg)
        pygame.draw.rect(self.bg, (255, 255, 255), (self.width/2 - 5, 0, 5, self.height))
        pygame.display.flip()
