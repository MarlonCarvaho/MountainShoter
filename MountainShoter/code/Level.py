# -*- coding: utf-8 -*-
import pygame
import sys

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Carrega as imagens do fundo
        self.entity_list.extend(EntityFactory.get_entity('fase01pt1'))

        # Toca a música da fase
        pygame.mixer.music.load('./asset/fase01.wav')
        pygame.mixer.music.play(-1)

    def run(self):
        # Cria o relógio para a tela não passar rápido demais
        clock = pygame.time.Clock()

        while True:
            # Trava o jogo em 60 FPS
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()  # Faz as imagens andarem para a esquerda
                self.window.blit(source=ent.surf, dest=ent.rect)

            pygame.display.flip()