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
            pygame.mixer.music.load('./asset/menu.wav')
            pygame.mixer.music.play(-1)

            self.window.fill((0, 0, 0))
            menu_return = menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if menu_return in [menu_option[0], menu_option[1], menu_option[2]]:
                # Inicia a Fase 1 e guarda o resultado
                level1 = Level(self.window, 'level1', menu_return)
                resultado = level1.run()

                # Se venceu a Fase 1 (e não for o modo Competitivo), vai para a Fase 2!
                if resultado == "WIN" and menu_return != menu_option[2]:
                    level2 = Level(self.window, 'level2', menu_return)
                    level2.run()

            elif menu_return == menu_option[4]:
                pygame.quit()
                sys.exit()

            pygame.display.update()