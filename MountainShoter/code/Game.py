import pygame
from Menu import Menu
from Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.menu = Menu(self.window)
        self.levels = [Level(self.window, "Fase 1")]

    def run(self):
        # Aqui entra o loop principal do jogo (While True)
        self.menu.run()
        self.levels[0].run()

if __name__ == "__main__":
    jogo = Game()
    jogo.run()