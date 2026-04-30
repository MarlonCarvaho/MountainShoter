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

        # --- CARREGA RECURSOS BASEADO NA FASE ---
        if self.name == 'level1':
            self.bg_list = EntityFactory.get_entity('fase01pt1')
            pygame.mixer.music.load('./asset/fase01.wav')
            self.difficulty = 1.0  # Dificuldade normal
        elif self.name == 'level2':
            self.bg_list = EntityFactory.get_entity('faze02')
            pygame.mixer.music.load('./asset/faze02.wav')
            self.difficulty = 1.3  # 30% mais difícil!

        pygame.mixer.music.play(-1)

        self.player_list = []
        self.enemy_list = []
        self.projectile_list = []

        self.player_list.append(EntityFactory.get_entity("Mago1", (100, 300)))

        if self.game_mode == menu_option[1]:
            self.player_list.append(EntityFactory.get_entity("Mago2", (100, 400)))
        elif self.game_mode == menu_option[2]:
            p2 = EntityFactory.get_entity("Mago2", (650, 300))
            p2.set_orientation(-1)
            self.player_list.append(p2)

        self.spawn_timer = 0
        self.game_over_timer = 0
        self.enemies_killed = 0
        self.survive_timer = 60 * 60

    def run(self):
        clock = pygame.time.Clock()
        font_timer = pygame.font.SysFont("Lucida Sans Typewriter", 18)
        font_hud = pygame.font.SysFont("Lucida Sans Typewriter", 24)

        while True:
            clock.tick(60)

            if self.survive_timer > 0:
                self.survive_timer -= 1

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
                    # Passa a dificuldade para o Factory gerar o inimigo mais forte!
                    self.enemy_list.append(EntityFactory.get_entity("Inimigo", (730, spawn_y), self.difficulty))

                    # O tempo de nascer novos inimigos também fica 30% mais rápido!
                    tempo_min = int(60 / self.difficulty)
                    tempo_max = int(150 / self.difficulty)
                    self.spawn_timer = random.randint(tempo_min, tempo_max)
                else:
                    self.spawn_timer -= 1

            for proj in self.projectile_list[:]:
                hit_something = False

                if proj.name == "magia":
                    for enemy in self.enemy_list[:]:
                        if proj.rect.colliderect(enemy.rect):
                            enemy.health -= 10
                            hit_something = True
                            if enemy.health <= 0:
                                self.enemy_list.remove(enemy)
                                self.enemies_killed += 1
                            break

                    if self.game_mode == menu_option[2]:
                        for player in self.player_list:
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
                                if self.game_mode == menu_option[1]:
                                    player.respawn_timer = 600
                            break

                if hit_something or proj.rect.left > 800 or proj.rect.right < 0:
                    if proj in self.projectile_list:
                        self.projectile_list.remove(proj)

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

                if not player.is_dead:
                    vida_porcentagem = max(0, player.health) / player.max_health
                    pygame.draw.rect(self.window, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
                    pygame.draw.rect(self.window, (0, 255, 0), (bar_x, bar_y, bar_width * vida_porcentagem, bar_height))
                    pygame.draw.rect(self.window, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 1)
                elif self.game_mode == menu_option[1] and player.respawn_timer > 0:
                    segundos = player.respawn_timer // 60
                    texto_timer = font_timer.render(f"Revive em: {segundos}s", True, (255, 255, 0))
                    self.window.blit(texto_timer, (bar_x, bar_y))

            if self.game_mode != menu_option[2]:
                segundos_restantes = max(0, self.survive_timer // 60)

                texto_tempo = font_hud.render(f"Tempo: {segundos_restantes}s", True, (255, 255, 255))
                self.window.blit(texto_tempo, (350, 10))

                texto_kills = font_hud.render(f"Abates: {self.enemies_killed}/10", True, (255, 255, 255))
                self.window.blit(texto_kills, (350, 35))

            # --- SISTEMA DE RETORNO DO RESULTADO ---
            is_game_over = False
            is_victory = False

            if self.game_mode == menu_option[0]:
                if self.player_list[0].is_dead: is_game_over = True
            elif self.game_mode == menu_option[1]:
                if self.player_list[0].is_dead and self.player_list[1].is_dead: is_game_over = True
            elif self.game_mode == menu_option[2]:
                if self.player_list[0].is_dead or self.player_list[1].is_dead: is_game_over = True

            if self.game_mode != menu_option[2]:
                if self.enemies_killed >= 10 or self.survive_timer <= 0:
                    is_victory = True

            if is_game_over or is_victory:
                self.game_over_timer += 1

                if is_victory and not is_game_over:
                    # Se for level 1, avisa que vai para a próxima fase. Se for level 2, avisa que zerou!
                    texto_msg = "INICIANDO FASE 2..." if self.name == 'level1' else "VOCÊ ZEROU O JOGO!"
                    texto_vitoria = font_hud.render(texto_msg, True, (0, 255, 0))
                    self.window.blit(texto_vitoria, (300, 300))

                if self.game_over_timer > 180:
                    # AGORA ELE DEVOLVE "WIN" SE GANHOU, OU "GAMEOVER" SE PERDEU
                    if is_victory and not is_game_over:
                        return "WIN"
                    else:
                        return "GAMEOVER"
            else:
                self.game_over_timer = 0

            pygame.display.flip()