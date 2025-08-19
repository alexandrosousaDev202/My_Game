import pygame
import sys 
from code.settings import *
from code.entities import Player, Inimigo, todos_sprites, inimigos, balas_jogador

class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        
        background_original = pygame.image.load(os.path.join(diretorio_assets, 'Level1Bg0.png')).convert()
        self.background = pygame.transform.scale(background_original, (LARGURA_TELA, ALTURA_TELA))
        
        self.background_rect = self.background.get_rect()
        self.start_new_game()

    def start_new_game(self):
        todos_sprites.empty()
        inimigos.empty()
        balas_jogador.empty()
        
        self.jogador = Player()
        todos_sprites.add(self.jogador)
        
        for _ in range(8):
            inimigo = Inimigo()
            todos_sprites.add(inimigo)
            inimigos.add(inimigo)

    def run(self):
        self.jogando = True
        while self.jogando:
            self.clock.tick(FPS)
            self.eventos()
            self.update()
            self.desenho()
        return "MENU"

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.jogador.atirar()

        todos_sprites.update()

        colisoes_tiro = pygame.sprite.groupcollide(inimigos, balas_jogador, True, True)
        for _ in colisoes_tiro:
            inimigo = Inimigo()
            todos_sprites.add(inimigo)
            inimigos.add(inimigo)

        colisoes_jogador = pygame.sprite.spritecollide(self.jogador, inimigos, False, pygame.sprite.collide_circle)
        if colisoes_jogador:
            self.jogando = False

    def desenho(self):
        self.window.blit(self.background, self.background_rect)
        todos_sprites.draw(self.window)
        pygame.display.flip()