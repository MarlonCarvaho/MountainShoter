import pygame
from EntityFactory import EntityFactory

class Level:
    def __init__(self, window: pygame.Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list = []

    def run(self) -> None:
        print(f"Executando {self.name}")