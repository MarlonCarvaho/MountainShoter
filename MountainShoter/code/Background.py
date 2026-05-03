#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        layer_number = int(name[-1])

        self.speed = layer_number + 1

    def move(self):
        self.rect.left -= self.speed

        if self.rect.right <= 0:
            self.rect.left += 1600