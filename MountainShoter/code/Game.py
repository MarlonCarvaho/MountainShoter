#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Menu import Menu
from code.Level import Level
from code.Score import Score
from code.const import menu_option


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 30)

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
                level1 = Level(self.window, 'level1', menu_return)
                status1, score1 = level1.run()

                if status1 == "WIN" and menu_return != menu_option[2]:
                    level2 = Level(self.window, 'level2', menu_return)
                    status2, score2 = level2.run()

                    if status2 == "WIN":
                        total_score = score1 + score2
                        name = self.get_player_name(total_score)
                        Score.save(name, total_score)

            elif menu_return == menu_option[3]:
                self.show_scores()

            elif menu_return == menu_option[4]:
                pygame.quit()
                sys.exit()

            pygame.display.update()

    def get_player_name(self, score):
        name = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) > 0:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10 and event.unicode.isprintable():
                            name += event.unicode

            self.window.fill((0, 0, 0))
            texto_titulo = self.font.render(f"NOVO RECORDE! Pontos: {score}", True, (0, 255, 0))
            self.window.blit(texto_titulo, (200, 200))

            texto_nome = self.font.render(f"Digite seu nome: {name}_", True, (255, 255, 255))
            self.window.blit(texto_nome, (200, 300))

            pygame.display.flip()

    def show_scores(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        return  # Volta pro menu principal

            self.window.fill((0, 0, 0))
            texto_titulo = self.font.render("TOP 7 MAIS RAPIDOS", True, (255, 255, 0))
            self.window.blit(texto_titulo, (250, 50))

            scores = Score.get_all()
            if not scores:
                texto_vazio = self.font.render("Nenhuma pontuacao ainda.", True, (255, 255, 255))
                self.window.blit(texto_vazio, (200, 150))
            else:
                for i, s in enumerate(scores):
                    texto = self.font.render(f"{i + 1}. {s['name']} - {s['score']} pts", True, (255, 255, 255))
                    self.window.blit(texto, (250, 150 + (i * 40)))

            texto_voltar = self.font.render("Pressione ESC para voltar", True, (150, 150, 150))
            self.window.blit(texto_voltar, (220, 500))

            pygame.display.flip()