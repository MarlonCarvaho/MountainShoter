#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random  # Precisamos importar o random para sortear os inimigos!

from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case "Mago1":
                return Player("mago1", position, player_type=1)

            case "Mago2":
                return Player("mago2", position, player_type=2)

            case "Inimigo":
                # Sorteia qual das 3 imagens de inimigo vai usar!
                nome_sorteado = random.choice(["inimigo1", "inimigo2", "inimigo3"])
                return Enemy(nome_sorteado, position)

            case "fase01pt1":
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'fase01pt{i}', (0, 0)))
                    list_bg.append(Background(f'fase01pt{i}', (800, 0)))

                return list_bg