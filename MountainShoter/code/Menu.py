#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Menu:
    def __init__(self, window):
        self.window = window

        # Carrega a imagem e redimensiona
        self.surf = pygame.image.load('./asset/menu.png')
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)

        # Carrega e dá o play na música (em loop infinito)
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)

    def run(self):
        # Apenas desenha a imagem de fundo na tela a cada frame
        self.window.blit(source=self.surf, dest=self.rect)

        # EXEMPLO DE USO: Chamando a função de texto para aparecer na tela.
        # Texto: "MOUNTAIN SHOOTER", Tamanho: 50, Cor: Branco (255, 255, 255), Posição Centro: x=400, y=100
        self.menu_text("MOUNTAIN SHOOTER", 50, (255, 255, 255), (400, 100))

    # Função puxada para fora do run() para fazer parte da classe
    def menu_text(self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple):
        # Usando SysFont para pegar a fonte direto do sistema
        text_font = pygame.font.SysFont('lucida sans typewriter', text_size)

        # Sintaxe corrigida: passando as variáveis diretas e usando True maiúsculo
        text_surf = text_font.render(text, True, text_color).convert_alpha()

        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)