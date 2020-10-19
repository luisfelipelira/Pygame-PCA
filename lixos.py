import pygame
import time
from random import randint

clock = pygame.time.Clock()
pygame.mixer.init()

LIXOVELOCIDADE = 2

class LixoL(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/LataLixo1.png'),
                    pygame.image.load('Imagens/jogo/LataLixo2.png'),
                    pygame.image.load('Imagens/jogo/Lixo1.png')]

        self.current_image = randint(0, 2)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(130, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y += LIXOVELOCIDADE


class LixoR(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/LataLixo1.png'),
                        pygame.image.load('Imagens/jogo/LataLixo2.png'),
                        pygame.image.load('Imagens/jogo/Lixo1.png')]

        self.current_image = randint(0, 2)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(810, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y += LIXOVELOCIDADE

class tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/LataLixo1.png'),
                    pygame.image.load('Imagens/jogo/LataLixo2.png'),
                    pygame.image.load('Imagens/jogo/Lixo1.png')]

        self.current_image = randint(0, 2)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(130, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y -= 5