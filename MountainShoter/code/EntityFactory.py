#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case "fase01pt1":
                list_bg = []
                for i in range(6):
                    # Imagem 1: Começa dentro da tela (posição 0)
                    list_bg.append(Background(f'fase01pt{i}', (0, 0)))
                    # Imagem 2: Começa logo atrás da primeira (posição 800)
                    list_bg.append(Background(f'fase01pt{i}', (800, 0)))

                return list_bg