#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.Projectile import Projectile


class Player(Entity):
    def __init__(self, name: str, position: tuple, player_type: int):
        super().__init__(name, position, size=(50, 50))
        self.player_type = player_type
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.shoot_delay = 0
        self.orientation = 1

        # --- NOVAS VARIÁVEIS DE VIDA/MORTE ---
        self.is_dead = False
        self.respawn_timer = 0

        # Guardamos a imagem dele vivo
        self.image_alive = self.surf
        # Carregamos a imagem dele morto direto da sua pasta asset e ajustamos o tamanho
        img_dead = pygame.image.load(f"./asset/mago{self.player_type}_morreu.png").convert_alpha()
        self.image_dead = pygame.transform.scale(img_dead, (50, 50))

    def set_orientation(self, orientation: int):
        # Uma função inteligente para virar o mago (vivo e morto) para a esquerda se necessário!
        self.orientation = orientation
        if self.orientation == -1:
            self.image_alive = pygame.transform.flip(self.image_alive, True, False)
            self.image_dead = pygame.transform.flip(self.image_dead, True, False)
            self.surf = self.image_alive

    def die(self):
        # O que acontece quando ele morre
        self.is_dead = True
        self.health = 0
        self.surf = self.image_dead  # Troca para a imagem caída no chão

    def revive(self):
        # O que acontece quando o timer chega a zero
        self.is_dead = False
        self.health = self.max_health
        self.surf = self.image_alive  # Levanta do chão!

    def move(self):
        # Se estiver morto, ele NÃO anda. Apenas conta o cronômetro para reviver.
        if self.is_dead:
            if self.respawn_timer > 0:
                self.respawn_timer -= 1
                if self.respawn_timer <= 0:
                    self.revive()
            return  # Interrompe a função move() aqui

        keys = pygame.key.get_pressed()

        if self.player_type == 1:
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < 600:
                self.rect.y += self.speed
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.right < 800:
                self.rect.x += self.speed

        elif self.player_type == 2:
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.bottom < 600:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < 800:
                self.rect.x += self.speed

        if self.shoot_delay > 0:
            self.shoot_delay -= 1

    def shoot(self):
        # Se estiver morto, não pode atirar
        if self.is_dead:
            return None

        self.shoot_delay = 30

        if self.orientation == 1:
            pos = (self.rect.right, self.rect.centery - 10)
            return Projectile("magia", pos, speed_x=10)
        else:
            pos = (self.rect.left - 30, self.rect.centery - 10)
            proj = Projectile("magia", pos, speed_x=-10)
            proj.surf = pygame.transform.flip(proj.surf, True, False)
            return proj