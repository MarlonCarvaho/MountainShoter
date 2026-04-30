#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
import random

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import menu_option


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.bg_list = EntityFactory.get_entity('fase01pt1')
        self.player_list = []
        self.enemy_list = []
        self.projectile_list = []

        self.player_list.append(EntityFactory.get_entity("Mago1", (100, 300)))

        if self.game_mode == menu_option[1]:
            self.player_list.append(EntityFactory.get_entity("Mago2", (100, 400)))

        elif self.game_mode == menu_option[2]:
            p2 = EntityFactory.get_entity("Mago2", (650, 300))
            p2.set_orientation(-1)  # Nova forma mais segura de virar o Mago 2!
            self.player_list.append(p2)

        self.spawn_timer = 0
        self.game_over_timer = 0  # Tempo que a tela fica parada antes de voltar ao menu

        pygame.mixer.music.load('./asset/fase01.wav')
        pygame.mixer.music.play(-1)

    def run(self):
        clock = pygame.time.Clock()
        # Fonte para o texto do timer de reviver
        font_timer = pygame.font.SysFont("Lucida Sans Typewriter", 18)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    for player in self.player_list:
                        if player.player_type == 1 and event.key == pygame.K_SPACE and player.shoot_delay == 0:
                            proj = player.shoot()
                            if proj: self.projectile_list.append(proj)
                        if player.player_type == 2 and event.key == pygame.K_RETURN and player.shoot_delay == 0:
                            proj = player.shoot()
                            if proj: self.projectile_list.append(proj)

            if self.game_mode != menu_option[2]:
                if self.spawn_timer <= 0:
                    spawn_y = random.randint(50, 500)
                    self.enemy_list.append(EntityFactory.get_entity("Inimigo", (730, spawn_y)))
                    self.spawn_timer = random.randint(60, 150)
                else:
                    self.spawn_timer -= 1

            # --- SISTEMA DE COLISÃO ---
            for proj in self.projectile_list[:]:
                hit_something = False

                if proj.name == "magia":
                    for enemy in self.enemy_list[:]:
                        if proj.rect.colliderect(enemy.rect):
                            enemy.health -= 10
                            hit_something = True
                            if enemy.health <= 0:
                                self.enemy_list.remove(enemy)
                            break

                    if self.game_mode == menu_option[2]:
                        for player in self.player_list:
                            # Agora checa se o jogador não está morto antes de tomar dano
                            if proj.rect.colliderect(player.rect) and not player.is_dead:
                                if (player.player_type == 1 and proj.speed_x < 0) or (
                                        player.player_type == 2 and proj.speed_x > 0):
                                    player.health -= 10
                                    hit_something = True
                                    if player.health <= 0:
                                        player.die()
                                    break

                elif proj.name == "magia_inimigo":
                    for player in self.player_list:
                        if proj.rect.colliderect(player.rect) and not player.is_dead:
                            player.health -= 10
                            hit_something = True
                            if player.health <= 0:
                                player.die()
                                # Se for modo Co-op, coloca 10 segundos de punição (600 frames)
                                if self.game_mode == menu_option[1]:
                                    player.respawn_timer = 600
                            break

                if hit_something or proj.rect.left > 800 or proj.rect.right < 0:
                    if proj in self.projectile_list:
                        self.projectile_list.remove(proj)

            # --- DESENHANDO NA TELA ---
            self.window.fill((0, 0, 0))

            for bg in self.bg_list:
                bg.move()
                self.window.blit(source=bg.surf, dest=bg.rect)

            for enemy in self.enemy_list:
                enemy.move()
                if enemy.shoot_delay == 0:
                    self.projectile_list.append(enemy.shoot())
                self.window.blit(source=enemy.surf, dest=enemy.rect)

            for proj in self.projectile_list:
                proj.move()
                self.window.blit(source=proj.surf, dest=proj.rect)

            for player in self.player_list:
                player.move()
                self.window.blit(source=player.surf, dest=player.rect)

                bar_width = 100
                bar_height = 15

                if player.player_type == 1:
                    bar_x, bar_y = 10, 10
                else:
                    if self.game_mode == menu_option[2]:
                        bar_x, bar_y = 690, 10
                    else:
                        bar_x, bar_y = 10, 30

                        # Se o jogador estiver vivo, desenha a barra normal
                if not player.is_dead:
                    vida_porcentagem = max(0, player.health) / player.max_health
                    pygame.draw.rect(self.window, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
                    pygame.draw.rect(self.window, (0, 255, 0), (bar_x, bar_y, bar_width * vida_porcentagem, bar_height))
                    pygame.draw.rect(self.window, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 1)

                # Se estiver morto e no modo Co-op com timer rodando, desenha o texto
                elif self.game_mode == menu_option[1] and player.respawn_timer > 0:
                    segundos = player.respawn_timer // 60  # Divide os frames para ter segundos reais
                    texto_timer = font_timer.render(f"Revive em: {segundos}s", True, (255, 255, 0))
                    self.window.blit(texto_timer, (bar_x, bar_y))

            # --- SISTEMA DE GAME OVER (VOLTAR AO MENU) ---
            is_game_over = False

            # Solo: Mago 1 morreu = Game Over
            if self.game_mode == menu_option[0]:
                if self.player_list[0].is_dead:
                    is_game_over = True

            # Coop: Os DOIS Magos morreram = Game Over
            elif self.game_mode == menu_option[1]:
                if self.player_list[0].is_dead and self.player_list[1].is_dead:
                    is_game_over = True

            # Competitivo: Qualquer um morreu = Game Over
            elif self.game_mode == menu_option[2]:
                if self.player_list[0].is_dead or self.player_list[1].is_dead:
                    is_game_over = True

            if is_game_over:
                self.game_over_timer += 1
                if self.game_over_timer > 180:  # Espera 3 segundos com os corpos no chão
                    return  # Quebra o ciclo, o que faz o jogo voltar automaticamente pro Menu!
            else:
                self.game_over_timer = 0  # Reseta o timer caso alguém seja revivido no Coop
            # ---------------------------------------------

            pygame.display.flip()