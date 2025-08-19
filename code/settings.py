
import os
import sys

LARGURA_TELA = 480
ALTURA_TELA = 600
FPS = 60


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o asset, funciona para dev e para PyInstaller """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    return os.path.join(base_path, relative_path)

diretorio_assets = resource_path("assets")
