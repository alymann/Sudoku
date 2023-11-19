import pygame
from constants import *


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = BOARD_SIZE
        self.height = BOARD_SIZE
        self.temp = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
        # Setter for this cell’s value

    def set_sketched_value(self, value):
        self.temp = value
        # Setter for this cell’s sketched value

    def draw(self):
        num = pygame.font.SysFont('Comic Sans MS', 40)
        x = self.col * SQUARE_SIZE
        y = self.row * SQUARE_SIZE
        color = (225, 198, 153)
        if self.selected:
            if self.value == 0:
                color = (195, 198, 245)
            else:
                color = (255, 80, 80)
        pygame.draw.rect(self.screen, color, (x, y, x + SQUARE_SIZE, y + SQUARE_SIZE))

        if self.temp != 0 and self.value == 0:
            text = num.render(str(self.temp), 0, (128, 128, 128))
            rect = text.get_rect(
                center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row))
            self.screen.blit(text, rect)
        elif not (self.value == 0):
            text = num.render(str(self.value), 0, (0, 0, 0))
            self.screen.blit(text, (
            x + (SQUARE_SIZE // 2 - text.get_width() / 2), y + (SQUARE_SIZE // 2 - text.get_height() / 2)))

    # Draws this cell, along with the value inside it.
    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.

    # Shows selected cell
    # if Board.select(self.row, self.col) == self.board[self.row][self.col]:
    # pygame.draw.rect(self.screen, (255, 0, 0), (x, y, gap, gap), 3)
