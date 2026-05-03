#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
from code.Entity import Entity
from code.Projectile import Projectile


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, difficulty: float = 1.0):
        super().__init__(name, position, size=(50, 50))

        # --- O SEGREDO ESTÁ AQUI ---
        # Espelha a imagem do inimigo para ele olhar para a esquerda (de frente pros magos!)
        self.surf = pygame.transform.flip(self.surf, True, False)
        # ---------------------------

        # Multiplica a vida pela dificuldade (Fase 1 = 1.0, Fase 2 = 1.3)
        self.health = int(30 * difficulty)
        self.speed_y = 3
        self.difficulty = difficulty

        # Atiram mais rápido dependendo da dificuldade
        self.shoot_delay = random.randint(int(90 / difficulty), int(180 / difficulty))

    def move(self):
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

        if self.shoot_delay > 0:
            self.shoot_delay -= 1

    def shoot(self):
        self.shoot_delay = random.randint(int(150 / self.difficulty), int(300 / self.difficulty))

        # Cria a magia do inimigo
        proj = Projectile("magia_inimigo", (self.rect.left, self.rect.centery - 10), speed_x=-7)

        # --- VIRA A MAGIA TAMBÉM ---
        # Espelha a imagem da magia do inimigo para ela voar com a ponta virada para a esquerda!
        proj.surf = pygame.transform.flip(proj.surf, True, False)
        # ---------------------------

        return proj