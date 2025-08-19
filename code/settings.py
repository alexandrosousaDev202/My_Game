
import os

LARGURA_TELA = 480
ALTURA_TELA = 600
FPS = 60


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


diretorio_jogo = os.path.dirname(os.path.dirname(__file__)) 
diretorio_assets = os.path.join(diretorio_jogo, 'assets')
