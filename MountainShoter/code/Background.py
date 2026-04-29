#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Tira o "zoom" forçando a imagem a ter o tamanho exato da tela
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        # Pega o último caractere do nome do arquivo para definir a velocidade
        # Ex: "fase01pt0" -> número 0. "fase01pt5" -> número 5.
        layer_number = int(name[-1])

        # Define a velocidade (Parallax). Quanto maior o número da imagem, mais rápida.
        self.speed = layer_number + 1

    def move(self):
        # Move a imagem para a esquerda
        self.rect.left -= self.speed

        # Se a imagem sair 100% da tela pela esquerda, ela volta para o final da fila à direita
        if self.rect.right <= 0:
            # Soma 1600 (800x2) para reposicionar a imagem atrás da sua "gêmea" perfeitamente
            self.rect.left += 1600