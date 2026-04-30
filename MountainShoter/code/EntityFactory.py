#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random

from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0), difficulty: float = 1.0):
        match entity_name:
            case "Mago1":
                return Player("mago1", position, player_type=1)

            case "Mago2":
                return Player("mago2", position, player_type=2)

            case "Inimigo":
                nome_sorteado = random.choice(["inimigo1", "inimigo2", "inimigo3"])
                # Passa a dificuldade para o inimigo!
                return Enemy(nome_sorteado, position, difficulty)

            case "fase01pt1":
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'fase01pt{i}', (0, 0)))
                    list_bg.append(Background(f'fase01pt{i}', (800, 0)))
                return list_bg

            case "faze02":
                # Lendo exatamente os arquivos da sua imagem: faze02pt01 até faze02pt06
                list_bg = []
                for i in range(1, 7):
                    list_bg.append(Background(f'faze02pt0{i}', (0, 0)))
                    list_bg.append(Background(f'faze02pt0{i}', (800, 0)))
                return list_bg