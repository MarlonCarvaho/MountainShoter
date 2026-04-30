#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Menu import Menu
from code.Level import Level
from code.const import menu_option

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        menu = Menu(self.window)

        while True:
            self.window.fill((0, 0, 0))
            menu_return = menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # AGORA ELE ACEITA OS 3 MODOS (0, 1 e 2)
            if menu_return in [menu_option[0], menu_option[1], menu_option[2]]:
                level = Level(self.window, 'level1', menu_return)
                level.run()
            elif menu_return == menu_option[4]:
                pygame.quit()
                sys.exit()

            pygame.display.update()