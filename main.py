
import pygame
from code.settings import *
from code.menu import Menu
from code.game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Meu Jogo de Nave")
        self.estado_jogo = "MENU"

    def run(self):
        while True:
            if self.estado_jogo == "MENU":
                menu = Menu(self.window)
                if menu.run() == "JOGAR":
                    self.estado_jogo = "JOGANDO"
            
            elif self.estado_jogo == "JOGANDO":
                game = Game(self.window)
                if game.run() == "MENU":
                    self.estado_jogo = "MENU"

if __name__ == "__main__":
    main = Main()
    main.run()
