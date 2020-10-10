import pygame
import shelve
from catador import Carro
from player import Player
from lixos import Lixo
import os


os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 980
HEIGHT = 720

pygame.init()
save = shelve.open('save')
pygame.display.set_caption("Trash Cleaner")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Iniciando imagens, sons e fontes e arquivos

titulo = pygame.image.load('imagens/menu/titulo.png')
fundo = pygame.image.load('imagens/menu/fundo.png')

jogar = pygame.image.load('imagens/menu/jogar.png')
jogaralt = pygame.image.load('imagens/menu/jogaralt.png')

sair = pygame.image.load('imagens/menu/sair.png')
sairalt = pygame.image.load('imagens/menu/sairalt.png')

config = pygame.image.load('imagens/menu/config.png')
configalt = pygame.image.load('imagens/menu/configalt.png')


# music = pygame.mixer.Sound('Sons/music.wav')
# passos = pygame.mixer.Sound('Sons/passos.wav')
def menu():
    # Coloca as imagens
    screen.blit(fundo, (0, 0))
    screen.blit(titulo, (WIDTH / 4.5, 0))
    screen.blit(jogar, (WIDTH / 3.1, 300))
    # screen.blit(jogaralt, (WIDTH / 4,0))
    screen.blit(sair, (WIDTH / 3, 460))
    # screen.blit(sairalt, (WIDTH / 4,0))
    screen.blit(config, (900, 0))
    # screen.blit(configalt, (800,0))
    pygame.display.flip()

    # Eventos clicáveis do Menu

    while pygame.event.wait() or pygame.event.get():

        # Pega a posição do mouse e
        # (Posição hitbox direita) > Posição X do mouse > (Posição hitbox esquerda) and (Posição hitbox baixo)
        # > Posição Y do mouse > (Posição hitbox cima) então:

        mouse = pygame.mouse.get_pos()

        if WIDTH / 3.1 + 359 > mouse[0] > WIDTH / 3.1 and 300 + 142 > mouse[1] > 300:
            screen.blit(jogaralt, (WIDTH / 3.3, 288))
            if pygame.mouse.get_pressed()[0]:

                # objetos

                objectGroup = pygame.sprite.Group()
                Player(objectGroup)
                Carro(objectGroup)
                Lixo(objectGroup)


                # Fundo
                bg = pygame.image.load('Imagens/jogo/fundosemobjetos.png').convert()
                bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
                bg_y = 0

                # Sounds
                andar = pygame.mixer.Sound('Sons/passos.wav')

                # Música

                # pygame.mixer_music.load("Sons/music.wav")
                # pygame.mixer.music.play(-1)

                # enemies_spd = 0

                clock = pygame.time.Clock()
                # def jogo():
                while True:
                    clock.tick(60)

                    # Faz o Fundo continuar infinito
                    bg_y1 = bg_y % bg.get_height()
                    bg_y += 2
                    screen.blit(bg, (0, bg_y1 - bg.get_height()))
                    if bg_y1 < HEIGHT:
                        screen.blit(bg, (0, bg_y1))
                        # Desenha os objetos
                        objectGroup.draw(screen)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                andar.play()
                            if event.key == pygame.K_ESCAPE:
                                menu()

                    # Update
                    objectGroup.update()
                    pygame.display.update()
                    screen.fill((0, 0, 0))
        else:
            screen.blit(jogar, (WIDTH / 3.1, 300))

        if WIDTH / 3 + 316 > mouse[0] > WIDTH / 3 and 460 + 115 > mouse[1] > 460:
            screen.blit(sairalt, (WIDTH / 3, 460))
            if pygame.mouse.get_pressed()[0]:
                quit()
        else:
            screen.blit(sair, (WIDTH / 3, 460))

        if 900 + 67 > mouse[0] > 900 and 0 + 67 > mouse[1] > 0:
            screen.blit(configalt, (899, -1))

        else:
            screen.blit(config, (900, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


menu()
pygame.quit()
