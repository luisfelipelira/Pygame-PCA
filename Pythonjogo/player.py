import pygame

WIDTH = 800
HEIGHT = 980


pygame.mixer.init()
andar = pygame.mixer.Sound('Sons/passos.wav')


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Imagens/boneco1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(480, 400, 100, 100)

    def update(self, *args):
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            self.rect.y -= 10
            andar.play()
        if comandos[pygame.K_DOWN]:
            self.rect.y += 10
            andar.play()
        if comandos[pygame.K_RIGHT]:
            self.rect.x += 10
            andar.play()
        if comandos[pygame.K_LEFT]:
            self.rect.x -= 10
            andar.play()

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIDTH:
            self.rect.bottom = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > HEIGHT:
            self.rect.right = HEIGHT
