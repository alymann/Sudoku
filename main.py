'''
finished 1. Implement three screens Game Start, Game-In-Progress, Game Over screen, and successfully switch between the screens.
finished 2. Implement three difficulty levels.
finished 3. Display the sudoku board with grid and values in cells.
finished 4. The user can play the game by selecting a cell, entering a number in a cell, and removing the number from a cell.
5. Implement the game win and game lose state in a correct way.
6. The code quality in terms of documentation and style is good in terms of readability and maintainability.
'''

import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *


def draw_game_start(screen):
  # Initialize title font
  start_title_font = pygame.font.Font(None, 100)
  button_font = pygame.font.Font(None, 70)
  # Color background
  screen.fill(BG_COLOR)

  # Initialize and draw title
  title_surface = start_title_font.render("Sudoku", 0, MAIN_COLOR)
  title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                   HEIGHT // 2 - 150))
  screen.blit(title_surface, title_rectangle)

  # Initialize buttons
  # Initialize text first
  easy_text = button_font.render("Easy", 0, WHITE)
  medium_text = button_font.render("Medium", 0, WHITE)
  hard_text = button_font.render("Hard", 0, WHITE)

  # Initialize & draw button background color and text
  easy_surface = pygame.Surface(
    (easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
  easy_surface.fill(MAIN_COLOR)
  easy_surface.blit(easy_text, (10, 10))

  medium_surface = pygame.Surface(
    (medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
  medium_surface.fill(MAIN_COLOR)
  medium_surface.blit(medium_text, (10, 10))

  hard_surface = pygame.Surface(
    (hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
  hard_surface.fill(MAIN_COLOR)
  hard_surface.blit(hard_text, (10, 10))

  # Initialize button rectangle
  easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
  medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 2 + 100))
  hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2,
                                                 HEIGHT // 2 + 200))

  # Draw buttons
  screen.blit(easy_surface, easy_rectangle)
  screen.blit(medium_surface, medium_rectangle)
  screen.blit(hard_surface, hard_rectangle)

  # Set difficulty based on user input
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if easy_rectangle.collidepoint(event.pos):
          return 20
        elif medium_rectangle.collidepoint(event.pos):
          return 40
        elif hard_rectangle.collidepoint(event.pos):
          return 50
    pygame.display.update()


def draw_in_game_ui(screen):
  button_font = pygame.font.SysFont(FONT_TYPE, 20)

  pygame.draw.rect(screen, WHITE, (0, BOARD_HEIGHT + 2, WIDTH, HEIGHT))
  reset_text = button_font.render("Reset", 0, WHITE)
  restart_text = button_font.render("Restart", 0, WHITE)
  exit_text = button_font.render("Exit", 0, WHITE)

  reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
  reset_surface.fill(MAIN_COLOR)
  reset_surface.blit(reset_text, (10, 10))

  restart_surface = pygame.Surface(
    (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
  restart_surface.fill(MAIN_COLOR)
  restart_surface.blit(restart_text, (10, 10))

  exit_surface = pygame.Surface(
    (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
  exit_surface.fill(MAIN_COLOR)
  exit_surface.blit(exit_text, (10, 10))

  reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 100, HEIGHT - 50))
  restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
  exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 92, HEIGHT - 50))

  screen.blit(reset_surface, reset_rectangle)
  screen.blit(restart_surface, restart_rectangle)
  screen.blit(exit_surface, exit_rectangle)
  return [reset_rectangle, restart_rectangle, exit_rectangle]


def draw_game_over(screen):
  start_title_font = pygame.font.Font(None, 100)
  button_font = pygame.font.Font(None, 70)
  # Color background
  screen.fill(BG_COLOR)
  game_over_surface = start_title_font.render("Game Lost :(", False, MAIN_COLOR)
  game_over_rectangle = game_over_surface.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 - 100))
  screen.blit(game_over_surface, game_over_rectangle)

  restart_text = button_font.render("Restart", 0, WHITE)

  restart_surface = pygame.Surface(
    (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
  restart_surface.fill(MAIN_COLOR)
  restart_surface.blit(restart_text, (10, 10))

  restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2,
                                                 HEIGHT // 2 + 100))
  screen.blit(restart_surface, restart_rectangle)

  game_over = True

  while game_over:
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if restart_rectangle.collidepoint(event.pos):
          main(screen)


def draw_congratulation(screen):

  start_title_font = pygame.font.Font(None, 100)
  button_font = pygame.font.Font(None, 70)
  # Color background
  screen.fill(BG_COLOR)
  game_won_surface = start_title_font.render("Game Won!", False, MAIN_COLOR)
  game_won_rectangle = game_won_surface.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 - 100))
  screen.blit(game_won_surface, game_won_rectangle)

  exit_text = button_font.render("Exit", 0, WHITE)

  exit_surface = pygame.Surface(
    (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
  exit_surface.fill(MAIN_COLOR)
  exit_surface.blit(exit_text, (10, 10))

  exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2,
                                                 HEIGHT // 2 + 100))
  screen.blit(exit_surface, exit_rectangle)

  congratulations_start = True

  while congratulations_start:
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if exit_rectangle.collidepoint(event.pos):
          sys.exit()

  #pygame.draw.rect(screen, (225, 198, 225), pygame.Rect(0, 0, 450, 450))


def main(screen):

  position = (0, 0)
  game_over = False
  difficulty = draw_game_start(screen)  # Calls function to draw start screen

  board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, difficulty)
  board.draw()

  while True:
    if board.is_full():
      if board.check_board():
        draw_congratulation(screen)
      else:
        draw_game_over(screen)
        break
    board.draw()
    a = draw_in_game_ui(screen)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        if event.pos[1] <= BOARD_HEIGHT:
          position = board.click(int(event.pos[1]), int(event.pos[0]))
          board.select(position[1], position[0])
        else:
          if a[0].collidepoint(event.pos):
            board.reset_to_original()
          elif a[1].collidepoint(event.pos):
            return False
          elif a[2].collidepoint(event.pos):
            sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          board.clear()
        elif event.key == pygame.K_RETURN:
          board.place_number()
          board.sketch(0)
        elif event.key == pygame.K_UP:
          y = position[1] - 1 if position[1] > 0 else 0
          position = (position[0], y)
        elif event.key == pygame.K_DOWN:
          y = position[1] + 1 if position[1] < BOARD_SIZE - 1 else BOARD_SIZE - 1
          position = (position[0], y)
        elif event.key == pygame.K_RIGHT:
          x = position[0] + 1 if position[0] < BOARD_SIZE - 1 else BOARD_SIZE - 1
          position = (x, position[1])
        elif event.key == pygame.K_LEFT:
          x = position[0] - 1 if position[0] > 0 else 0
          position = (x, position[1])
        else:
          if event.key == pygame.K_1:
            board.sketch(1)
          elif event.key == pygame.K_2:
            board.sketch(2)
          elif event.key == pygame.K_3:
            board.sketch(3)
          elif event.key == pygame.K_4:
            board.sketch(4)
          elif event.key == pygame.K_5:
            board.sketch(5)
          elif event.key == pygame.K_6:
            board.sketch(6)
          elif event.key == pygame.K_7:
            board.sketch(7)
          elif event.key == pygame.K_8:
            board.sketch(8)
          elif event.key == pygame.K_9:
            board.sketch(9)
        board.select(position[1], position[0])

if __name__ == '__main__':
  chip = 'x'

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Sudoku")
  while True:
    if main(screen) == False:
      continue
