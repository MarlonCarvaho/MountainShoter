#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    # Adicionamos o 'size' aqui
    def __init__(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()

        # Se passarmos um tamanho, o Pygame espreme a imagem para caber nele!
        if size:
            self.surf = pygame.transform.scale(self.surf, size)

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass