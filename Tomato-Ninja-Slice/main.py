"""apesar do erro  a seguir, o jogo está funcionando: 

#inicioErro 7/10
File "c:\Users\Aluno.SS-347130.002\Desktop\Tomato-Ninja-Slice\main.py", line 58, in main_menu
    import  tomato_ninja.py
ModuleNotFoundError: No module named 'tomato_ninja.py'; 'tomato_ninja' is not a package
PS C:\Users\Aluno.SS-347130.002\Desktop\Tomato-Ninja-Slice> 
#fimErro 7/10
"""

import pygame
import sys

pygame.init()

# Configurações da tela
WIDTH = 1000
HEIGHT = 500
FPS = 30
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Menu do Jogo')
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

def draw_text(text, size, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def show_authors():
    while True:
        screen.fill(RED)
        draw_text("Autores", FONT_SIZE, WIDTH / 2, HEIGHT / 4, WHITE)
        draw_text("Carolina Murtinho", FONT_SIZE, WIDTH / 2, HEIGHT / 2 - 50, WHITE)
        draw_text("Maria Vilbert", FONT_SIZE, WIDTH / 2, HEIGHT / 2, WHITE)
        draw_text("Sophia Martins", FONT_SIZE, WIDTH / 2, HEIGHT / 2 + 50, WHITE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

def main_menu():
    while True:
        screen.fill(RED)
        draw_text("Iniciar", FONT_SIZE, WIDTH / 2, HEIGHT / 3, WHITE)
        draw_text("Autores", FONT_SIZE, WIDTH / 2, HEIGHT / 2, WHITE)
        draw_text("Sair", FONT_SIZE, WIDTH / 2, HEIGHT * 2 / 3, WHITE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if WIDTH / 2 - FONT_SIZE < mouse_pos[0] < WIDTH / 2 + FONT_SIZE and HEIGHT / 3 - FONT_SIZE / 2 < mouse_pos[1] < HEIGHT / 3 + FONT_SIZE / 2:
                    # Iniciar o jogo
                    pygame.quit()
                    import  tomato_ninja.py
                    tomato_ninja.main()
                elif WIDTH / 2 - FONT_SIZE < mouse_pos[0] < WIDTH / 2 + FONT_SIZE and HEIGHT / 2 - FONT_SIZE / 2 < mouse_pos[1] < HEIGHT / 2 + FONT_SIZE / 2:
                    # Mostrar autores
                    show_authors()
                elif WIDTH / 2 - FONT_SIZE < mouse_pos[0] < WIDTH / 2 + FONT_SIZE and HEIGHT * 2 / 3 - FONT_SIZE / 2 < mouse_pos[1] < HEIGHT * 2 / 3 + FONT_SIZE / 2:
                    pygame.quit()
                    sys.exit()

        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()

