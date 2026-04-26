#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys  # Importante colocar isso no topo para o sys.exit() funcionar lá embaixo

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display_set_mode(size=(800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()
            #        quit()


