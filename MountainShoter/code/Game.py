#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Menu import Menu
from code.Level import Level  # O L agora é maiúsculo!
from code.const import WIN_WIDTH, menu_option


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        menu = Menu(self.window)

        while True:
            self.window.fill((0, 0, 0))

            # Pega a escolha do jogador
            menu_return = menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Checa qual opção foi escolhida
            if menu_return == menu_option[0]:
                # Inicia a fase 1
                level = Level(self.window, 'level1', menu_return)
                level.run()
            elif menu_return == menu_option[4]:
                # Sai do jogo
                pygame.quit()
                sys.exit()

            pygame.display.update()