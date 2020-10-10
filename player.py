import pygame
import time

WIDTH = 720
HEIGHT = 980

clock = pygame.time.Clock()
pygame.mixer.init()
andar = pygame.mixer.Sound('Sons/passos.wav')


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/boneco1.png'),
                       pygame.image.load('Imagens/jogo/boneco2.png')]

        self.current_image = 0
        self.image = pygame.image.load('Imagens/jogo/boneco1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(460, 570, 100, 100)

    def update(self, *args):
        comandos = pygame.key.get_pressed()
        self.current_image = (self.current_image + 1) % 2
        self.image = self.images[self.current_image]
        if comandos[pygame.K_UP]:
            self.rect.y -= 10
        if comandos[pygame.K_DOWN]:
            self.rect.y += 10
        if comandos[pygame.K_RIGHT]:
            self.rect.x += 10
        if comandos[pygame.K_LEFT]:
            self.rect.x -= 10

        # Limitando area do personagem andar
        if self.rect.top < 200:
            self.rect.top = 200
        if self.rect.bottom > WIDTH - 20:
            self.rect.bottom = WIDTH - 20
        if self.rect.left < 120:
            self.rect.left = 120
        if self.rect.right > 895:
            self.rect.right = 895
