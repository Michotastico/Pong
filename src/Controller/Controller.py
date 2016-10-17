#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

from src.Controller.Collision import Collision
from src.Controller.Keyboard import Keyboard
from src.Model.Ball import Ball
from src.Model.Bar import Bar
from src.Model.Counter import Counter
from src.View.Window import Window

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Controller:
    def __init__(self):
        self.height = 400
        self.width = 500

        pygame.init()
        self.win = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Pong')

        self.font = pygame.font.SysFont('Arial', 25)
        icon = pygame.image.load('images/p.png')
        pygame.display.set_icon(icon)

        initial_y = (self.height - 50)/2
        self.bar_one = Bar(10, initial_y)
        self.bar_two = Bar(self.width - 15, initial_y)

        self.ball = Ball(self.width/2 - 10, (self.height - 10)/2, 5, 10)

        self.counter_one = Counter(self.width/2, self.font, True)
        self.counter_two = Counter(self.width/2, self.font, False)

        self.window = Window(self.win, self.bar_one, self.bar_two, self.ball, self.counter_one, self.counter_two)

        self.keyboard = Keyboard(self.bar_one, self.bar_two, self.height)
        self.collision = Collision(self.width, self.height, self.bar_one, self.bar_two, self.ball,
                                   self.counter_one, self.counter_two)

    def update(self):
        self.window.clean()
        self.window.draw()

        self.keyboard.get_event()

        self.bar_one.update()
        self.bar_two.update()
        self.ball.update()

        self.collision.check_collision()









