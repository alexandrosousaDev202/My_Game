import pygame
from code.settings import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.fonte_jogo = pygame.font.match_font('arial')
        
        menu_bg_original = pygame.image.load(os.path.join(diretorio_assets, 'MenuBg.png')).convert()
        self.menu_background = pygame.transform.scale(menu_bg_original, (LARGURA_TELA, ALTURA_TELA))
        
        self.background_rect = self.menu_background.get_rect()
        
       
        pygame.mixer.music.load(os.path.join(diretorio_assets, 'Level1.mp3'))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)

    def desenhar_texto(self, text, size, x, y):
        fonte = pygame.font.Font(self.fonte_jogo, size)
        text_surface = fonte.render(text, True, BRANCO)
        text_rect = text_surface.get_rect(midtop=(x, y))
        self.window.blit(text_surface, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        return "JOGAR" 
            
            
            self.window.blit(self.menu_background, self.background_rect)
            self.desenhar_texto("Jogo de Nave", 64, LARGURA_TELA / 2, ALTURA_TELA / 4)
            self.desenhar_texto("Setas para mover, Espaço para atirar", 22, LARGURA_TELA / 2, ALTURA_TELA / 2)
            self.desenhar_texto("Pressione ENTER para começar", 18, LARGURA_TELA / 2, ALTURA_TELA * 3 / 4)
            
            pygame.display.flip()