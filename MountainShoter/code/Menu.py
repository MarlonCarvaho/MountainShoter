import pygame
import sys

from code.const import color_vermelho, color_branco, menu_option, color_azul

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)

        self.opcao_selecionada = 0

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font('./asset/Creepster-Regular.ttf', text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    def normal_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = font.render(text, True, text_color).convert_alpha()
        self.window.blit(source=text_surf, dest=text_pos)

    def run(self):
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.opcao_selecionada < len(menu_option) - 1:
                            self.opcao_selecionada += 1

                    if event.key == pygame.K_UP:
                        if self.opcao_selecionada > 0:
                            self.opcao_selecionada -= 1

                    if event.key == pygame.K_RETURN:
                        return menu_option[self.opcao_selecionada]

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "jogo de terror", color_vermelho, (400, 150))

            for i in range(len(menu_option)):
                if i == self.opcao_selecionada:
                    self.menu_text(30, menu_option[i], color_azul, (400, 250 + 30 * i))
                else:
                    self.menu_text(30, menu_option[i], color_branco, (400, 250 + 30 * i))


            self.normal_text(15, "CONTROLES:", color_vermelho, (10, 500))
            self.normal_text(15, "P1: W,A,S,D (Move) | ESPAÇO (Atira)", color_branco, (10, 520))
            self.normal_text(15, "P2: SETAS (Move)   | ENTER (Atira)", color_branco, (10, 540))
            # ----------------------------------------------

            pygame.display.flip()