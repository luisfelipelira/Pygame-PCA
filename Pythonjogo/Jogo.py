import os

import pygame

from catador import Carro
from Mapa import Cenario
from player import Player

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

fps = 60

# Resolução

WIDTH = 800
HEIGHT = 980

# objetos

objectGroup = pygame.sprite.Group()
player = Player(objectGroup)
catador = Carro(objectGroup)

# Janela

janela = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Trash Cleaner")

# Fundo
fundo_Group = pygame.sprite.Group()
fundo = Cenario("Imagens/fundoinf.png")
fundo_Group.add(fundo)

# Sounds
andar = pygame.mixer.Sound('Sons/passos.wav')

# Música

# pygame.mixer_music.load("Sons/music.wav")
# pygame.mixer.music.play(-1)


clock = pygame.time.Clock()
janela_aberta = True
while janela_aberta:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = janela_aberta = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                andar.play()

    # Update
    fundo.update()
    objectGroup.update()
    pygame.display.update()
    janela.fill((0, 0, 0))

    # Desenhar
    fundo_Group.draw(janela)
    objectGroup.draw(janela)
pygame.quit()
