#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity

class Projectile(Entity):
    def __init__(self, name: str, position: tuple, speed_x: int):

        super().__init__(name, position, size=(30, 15))
        self.speed_x = speed_x

    def move(self):
        self.rect.x += self.speed_x