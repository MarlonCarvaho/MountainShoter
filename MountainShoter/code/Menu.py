import pygame
import sys

from code.const import color_vermelho, color_branco, menu_option


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.surf = pygame.transform.scale(self.surf, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Troque "SysFont" por "Font" e coloque o caminho do arquivo
        text_font = pygame.font.Font('./asset/Creepster-Regular.ttf', text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.blit(source=self.surf, dest=self.rect)

            #self.menu_text(30, "Meu Jogo", color_branco, (400, 300))
            self.menu_text(50," jogo de terro",color_vermelho,(400,200) )

            for i in range(len(menu_option)):
                self.menu_text( 30,menu_option[i],color_branco,(400,300 +30 *i))
            pygame.display.flip()