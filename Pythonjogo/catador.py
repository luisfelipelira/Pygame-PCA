import pygame
import math

WIDTH = 720
HEIGHT = 980

class Carro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('Imagens/caminhãodelixo.png')
        self.image = pygame.transform.scale(self.image, [140, 330])
        self.rect = pygame.Rect(440, 10, 100, 100)
        self.timer = 0

    def update(self, *args):
        self.timer += 0.02
        self.rect.x = 35

        self.rect.x = 395 + math.sin(self.timer) * 225

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 750:
            self.rect.right = 750
