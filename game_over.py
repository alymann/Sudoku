import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *

def draw_game_over(screen):
    print('Game Over')
    game_over_font = pygame.font.Font(None, 100)
    screen.fill(BG_COLOR)
    # if winner != 0:
    #     text = f'Player {winner} wins!'
    # else:
    #     text = "No one wins!"
    game_over_surf = game_over_font.render("Game Over", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(
         center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)



    restart_surf = game_over_font.render(
        'Press r to play again...', 0, LINE_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.K_r:
            # sys.exit()
            draw_game_start(screen)
            # this wouldn't restart it would (hopefully) take back to menu selection
            # restart with same random generator to replay last game again??
    restart_rect = restart_surf.get_rect(
         center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    # #  Added key to return to main menu
    # menu_surf = game_over_font.render(
    #     'Press m to return to the main menu...', 0, LINE_COLOR)
    # menu_rect = menu_surf.get_rect(
    #     center=(WIDTH // 2, HEIGHT // 2 + 150))
    # screen.blit(menu_surf, menu_rect)

#AG
