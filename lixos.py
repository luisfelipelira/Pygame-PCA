import pygame as pg
from random import randint
from menu import screen

WIDTH = 980
HEIGHT = 720
pg.font.init()
pg.mixer.init()


lixo_speed = 0
lixo_x, lixo_y = 40, 54
lixo1_y = randint(-HEIGHT, -lixo_y)  # Posição do carro vermelho (lado esquerdo).
lixo2_y = randint(-HEIGHT, -lixo_y)  # Posição do carro amarelo (lado direito).
lixo3_y = randint(-HEIGHT, -lixo_y)  # Posição do carro azul (centro).


lixo_x= int(WIDTH / 2)


lixo_img = [pg.image.load('Imagens/jogo/LataLixo1.png'),
            pg.image.load('Imagens/jogo/LataLixo2.png'),
            pg.image.load('Imagens/jogo/Lixo1.png')]


lixo1_y += lixo_speed + 5
lixo2_y += lixo_speed + 2
lixo3_y += lixo_speed + 4
if lixo1_y > HEIGHT:
    lixo1_y = randint(-2500, - 2000)
if lixo2_y > HEIGHT:
    lixo2_y = randint(-1000, -750)
if lixo3_y > HEIGHT:
    lixo3_y = randint(-1750, -1250)

def lixo():
    screen.blit(lixo_img[1], (lixo_x - 115, lixo_y))
    screen.blit(lixo_img[2], (lixo_x - int(lixo_x / 2), lixo2_y))
    screen.blit(lixo_img[3], (lixo_x + 60, lixo_y))


