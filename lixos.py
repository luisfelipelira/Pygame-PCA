import pygame
import time
from random import randint

WIDTH = 720
HEIGHT = 980

clock = pygame.time.Clock()
pygame.mixer.init()
esteira = 0


class Lixo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/LataLixo1.png'),
                       pygame.image.load('Imagens/jogo/LataLixo2.png'),
                       pygame.image.load('Imagens/jogo/Lixo1.png')]

        self.current_image = randint(0, 2)
        self.image = pygame.image.load('Imagens/jogo/boneco1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(130, -250, 100, 100)

    def update(self, *args):
        self.image = self.images[self.current_image]
        if esteira == 0:
            self.rect.y += 2
        else:
            self.rect.y = 0
