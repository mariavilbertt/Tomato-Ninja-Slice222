import pygame
import sys
import os
import random

# Configurações do jogo
player_lives = 3
score = 0
fruits = ['melon', 'orng', 'app', 'guava', 'bomb']

# Inicialização do Pygame e criação da janela
WIDTH = 1000
HEIGHT = 500
FPS = 12

pygame.init()
pygame.display.set_caption('TOMATO NINJA!')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

background = pygame.image.load('bg.jpg')  # Imagem de fundo
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)
score_text = font.render('Score : ' + str(score), True, WHITE)  # Texto do placar

# Função para gerar frutas aleatórias
def generate_random_fruits(fruit):
    fruit_path = fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),
        'y': 800,
        'speed_x': random.randint(-10, 10),
        'speed_y': random.randint(-80, -60),
        'throw': random.random() >= 0.75,
        't': 0,
        'hit': False,
    }

# Dicionário para armazenar dados das frutas
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

# Função para desenhar texto na tela
def draw_text(display, text, size, x, y):
    # Usar o objeto de fonte diretamente em vez de criar uma nova instância
    text_font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), size)
    text_surface = text_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)

# Função para desenhar vidas do jogador
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()
        img_rect.x = int(x + 35 * i)
        img_rect.y = y
        display.blit(img, img_rect)

# Função para mostrar a tela de game over
def show_gameover_screen():
    gameDisplay.blit(background, (0, 0))
    draw_text(gameDisplay, "TOMATO NINJA!", 90, WIDTH / 2, HEIGHT / 4)
    if not game_over:
        draw_text(gameDisplay, "Score : " + str(score), 50, WIDTH / 2, HEIGHT / 2)
    draw_text(gameDisplay, "PRESSIONE UMA TECLA PARA INICIAR!", 36, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

# Loop principal do jogo
first_round = True
game_over = True
game_running = True
while game_running:
    if game_over:
        if first_round:
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        score = 0
        draw_lives(gameDisplay, 690, 5, player_lives, 'r_h.png')  # Ajuste do caminho da imagem
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))
    score_text = font.render('Score : ' + str(score), True, WHITE)
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'r_h.png')  # Ajuste do caminho da imagem
    
    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']
            value['y'] += value['speed_y']
            value['speed_y'] += (1 * value['t'])
            value['t'] += 1
            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_fruits(key)
            
            current_position = pygame.mouse.get_pos()
            if not value['hit'] and value['x'] < current_position[0] < value['x'] + 60 \
                    and value['y'] < current_position[1] < value['y'] + 60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives < 0:
                        show_gameover_screen()
                        game_over = True
                else:
                    half_fruit_path = "h_" + key + ".png"
                    value['img'] = pygame.image.load(half_fruit_path)
                    value['speed_x'] += 10
                    score += 1
                    score_text = font.render('Score : ' + str(score), True, WHITE)
                value['hit'] = True
        else:
            generate_random_fruits(key)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()