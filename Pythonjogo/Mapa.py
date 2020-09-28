import pygame

WIDTH = 800
HEIGHT = 980


class Cenario(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.bg = pygame.image.load("Imagens/fundoinf.png")
        self.image = self.bg
        self.rect = self.image.get_rect()
        self.rect.center = 490, 78

    def update(self):
        self.rect[1] += 1

    def is_off_screen(self):
        return self.rect[0] < - (self.rect[2])