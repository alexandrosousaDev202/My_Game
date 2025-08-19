
import pygame
import random
import os
from code.settings import *

todos_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
balas_jogador = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_img_original = pygame.image.load(os.path.join(diretorio_assets, 'Player1.png')).convert_alpha()
        self.image = pygame.transform.scale(player_img_original, (60, 48))
        self.rect = self.image.get_rect(centerx=LARGURA_TELA / 2, bottom=ALTURA_TELA - 20)
        self.velocidade_x = 0
        self.ultimo_tiro = pygame.time.get_ticks()
        self.cadencia_tiro = 250

    def update(self):
        self.velocidade_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]: self.velocidade_x = -8
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]: self.velocidade_x = 8
        self.rect.x += self.velocidade_x
        if self.rect.right > LARGURA_TELA: self.rect.right = LARGURA_TELA
        if self.rect.left < 0: self.rect.left = 0

    def atirar(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_tiro > self.cadencia_tiro:
            self.ultimo_tiro = agora
            bala = Bala(self.rect.centerx, self.rect.top, 'Player1Shot.png')
            todos_sprites.add(bala)
            balas_jogador.add(bala)

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        tipo_inimigo = random.choice(['Enemy1.png', 'Enemy2.png'])
        inimigo_img_original = pygame.image.load(os.path.join(diretorio_assets, tipo_inimigo)).convert_alpha()
        self.image = pygame.transform.scale(inimigo_img_original, (50, 40))
        self.rect = self.image.get_rect(x=random.randrange(LARGURA_TELA - 50), y=random.randrange(-150, -100))
        self.velocidade_y = random.randrange(1, 4)
        self.velocidade_x = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.velocidade_y
        self.rect.x += self.velocidade_x
        if self.rect.top > ALTURA_TELA + 10 or self.rect.left < -25 or self.rect.right > LARGURA_TELA + 20:
            self.rect.x = random.randrange(LARGURA_TELA - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidade_y = random.randrange(1, 4)

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_bala):
        super().__init__()
        bala_img_original = pygame.image.load(os.path.join(diretorio_assets, imagem_bala)).convert_alpha()
        self.image = pygame.transform.scale(bala_img_original, (15, 25))
        self.rect = self.image.get_rect(centerx=x, bottom=y)
        self.velocidade_y = -10

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.bottom < 0:
            self.kill()