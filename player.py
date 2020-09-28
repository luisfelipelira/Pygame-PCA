import pygame


WIDTH = 720
HEIGHT = 980


clock = pygame.time.Clock()
pygame.mixer.init()
andar = pygame.mixer.Sound('Sons/passos.wav')


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/boneco1.png'),
                       pygame.image.load('Imagens/boneco2.png')]

        self.current_image = 0
        self.image = pygame.image.load('Imagens/boneco1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(480, 400, 100, 100)

    def update(self, *args):
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            self.rect.y -= 10
            self.current_image = (self.current_image + 1) % 2
            self.image = self.images[self.current_image]
        if comandos[pygame.K_DOWN]:
            self.rect.y += 10
            self.current_image = (self.current_image + 1) % 2
            self.image = self.images[self.current_image]
        if comandos[pygame.K_RIGHT]:
            self.rect.x += 10
            self.current_image = (self.current_image + 1) % 2
            self.image = self.images[self.current_image]
        if comandos[pygame.K_LEFT]:
            self.rect.x -= 10
            self.current_image = (self.current_image + 1) % 2
            self.image = self.images[self.current_image]

        if self.rect.top < 200:
            self.rect.top = 200
        if self.rect.bottom > WIDTH+180:
            self.rect.bottom = WIDTH+180
        if self.rect.left < 65:
            self.rect.left = 65
        if self.rect.right > HEIGHT:
            self.rect.right = HEIGHT
