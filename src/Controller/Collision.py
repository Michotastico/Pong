#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Collision:
    def __init__(self, width, height, bar_one, bar_two, ball, counter_1, counter_2):
        self.width = width
        self.height = height
        self.bar_one = bar_one
        self.bar_two = bar_two
        self.ball = ball
        self.counter_one = counter_1
        self.counter_two = counter_2

    def check_collision(self):
        if self.bar_one.get_y() < 0:
            self.bar_one.set_y(0)
        elif self.bar_one.get_y() > self.height - 50:
            self.bar_one.set_y(self.height - 50)

        if self.bar_two.get_y() < 0:
            self.bar_two.set_y(0)
        elif self.bar_two.get_y() > self.height - 50:
            self.bar_two.set_y(self.height - 50)
        if self.ball.get_y() < 0:
            self.ball.set_y(0)
            self.ball.set_vy(-self.ball.get_vy())
        elif self.ball.get_y() > self.height - 10:
            self.ball.set_y(self.height - 10)
            self.ball.set_vy(-self.ball.get_vy())

        if self.ball.get_x() < 0:
            self.ball.set_x(0)
            self.ball.set_vx(-self.ball.get_vx())
            self.counter_two.add()
        elif self.ball.get_x() > self.width - 10:
            self.ball.set_x(self.width - 10)
            self.ball.set_vx(-self.ball.get_vx())
            self.counter_one.add()

        if self.bar_one.get_x() <= self.ball.get_x() <= (self.bar_one.get_x() + 5) \
                and self.bar_one.get_y() <= self.ball.get_y() <= (self.bar_one.get_y() + 50):
            self.ball.set_vx(-self.ball.get_vx())

        elif self.bar_two.get_x() <= self.ball.get_x() <= (self.bar_two.get_x() + 5) \
                and self.bar_two.get_y() <= self.ball.get_y() <= (self.bar_two.get_y() + 50):
            self.ball.set_vx(-self.ball.get_vx())
