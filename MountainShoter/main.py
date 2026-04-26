import sys

import pygame

print("Que comece o jogo")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print("Que comece o jogo")

print("começa a carregar")
while True:
    # chegando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("cteste do github")
            pygame.quit() # esse fecha a janela
            sys.exit() # esse encerra a janela
