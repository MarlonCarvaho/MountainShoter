import pygame
from Player import Player
from Enemy import Enemy
from Background import Background

class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str):
        surf = pygame.Surface((50, 50))
        rect = surf.get_rect()
        
        if entity_type == "player":
            return Player("Heroi", surf, rect)
        elif entity_type == "enemy":
            return Enemy("Monstro", surf, rect)
        return None