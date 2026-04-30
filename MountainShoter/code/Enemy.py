#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
from code.Entity import Entity
from code.Projectile import Projectile

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # Tamanho do inimigo ajustado
        super().__init__(name, position, size=(50, 50))
        self.health = 30
        self.speed_y = 3
        self.shoot_delay = random.randint(30, 90)

    def move(self):
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

        if self.shoot_delay > 0:
            self.shoot_delay -= 1

    def shoot(self):
        self.shoot_delay = random.randint(60, 120)
        return Projectile("magia_inimigo", (self.rect.left, self.rect.centery - 10), speed_x=-7)