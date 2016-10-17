#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Keyboard:
    def __init__(self, bar_one, bar_two, height):
        self.bar_one = bar_one
        self.bar_two = bar_two
        self.height = height

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_UP:
                    self.bar_one.set_vy(-10)
                    self.bar_two.set_vy(-10)

                elif event.key == pygame.K_DOWN:
                    self.bar_one.set_vy(10)
                    self.bar_two.set_vy(10)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.bar_one.set_vy(0)
                    self.bar_two.set_vy(0)

                elif event.key == pygame.K_DOWN:
                    self.bar_one.set_vy(0)
                    self.bar_two.set_vy(0)

