#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Menu import Menu
from code.const import WIN_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        menu = Menu(self.window)

        while True:
            self.window.fill((0, 0, 0))
            menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()