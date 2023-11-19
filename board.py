'''
* Click
* Sketch value
* Sk - value
* Three buttons
*
'''

import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator, generate_sudoku
from constants import *


class Board:

  # Constructor for the Board class.
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.rows = BOARD_SIZE
    self.cols = BOARD_SIZE
    self.difficulty = difficulty
    self.model = None
    self.generator = generate_sudoku(BOARD_SIZE, difficulty)
    self.position = (0, 0)
    self.cells = [[None] * BOARD_SIZE for i in range(BOARD_SIZE)]

    # pointer to position on the board
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        # setting up the sudoku board
        self.cells[i][j] = Cell(self.generator[i][j], i, j, screen)

  def draw(self):
    for x in range(self.rows):
      for y in range(self.cols):
        self.cells[y][x].draw()
      cell_size = 50
    for i in range(self.rows + 1):
      line_width = 1
      # every third line make line bold
      if i % 3 == 0:
        line_width = 3
      pygame.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0),
                       (i * cell_size, cell_size * self.cols), line_width)
    for j in range(self.cols + 1):
      line_width = 1
      if j % 3 == 0:
        line_width = 3
      pygame.draw.line(self.screen, (0, 0, 0), (0, j * cell_size),
                       (cell_size * self.rows, j * cell_size), line_width)


# Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
# Draws every cell on this board.

  def select(self, row, col):
    self.cells[self.position[0]][self.position[1]].selected = False
    self.position = (row, col)
    self.cells[row][col].selected = True

  # Marks the cell at (row, col) in the board as the current selected cell.
  # Once a cell has been selected, the user can edit its value or sketched value.

  def click(self, x, y):
    cell_size = 50  # pls discuss
    cell_x = int(x / cell_size)
    cell_y = int(y / cell_size)
    cell_x = 0 if cell_x < 0 else cell_x
    cell_x = BOARD_SIZE - 1 if cell_x > BOARD_SIZE - 1 else cell_x
    cell_y = 0 if cell_y < 0 else cell_y
    cell_y = BOARD_SIZE - 1 if cell_y > BOARD_SIZE - 1 else cell_y
    return (cell_y, cell_x)

  # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.

  def clear(self):
    row = self.position[0]
    col = self.position[1]
    if self.cells[row][col].value == 0:
      self.cells[row][col].set_sketched_value(0)
      self.cells[row][col].set_cell_value(0)
    '''
    how are we differentiating values filled in by uesr and vals filled in auto?
    put in if statement, if done by user run code, if not user cant change cell
    '''

  # Clears  the  value  cell.  Note  that  the  user  can only  remove  the  cell  values  and  sketched  value that  are filled by themselves.

  def sketch(self, value):
    row = self.position[0]
    col = self.position[1]
    if self.cells[row][col].value == 0:
      self.cells[row][col].set_sketched_value(value)
    """
    if auto filled in, don't need to sketch
    """

  # Sets the sketched value of the current selected cell equal to user entered value.
  # It will be displayed at the top left corner of the cell using the draw() function.

  def place_number(self):
    row = self.position[0]
    col = self.position[1]
    if self.cells[row][col].value == 0:
      cell = self.cells[row][col]
      cell.set_cell_value(cell.temp)
    """
    check if auto filled in
    """

  # Sets the value of the current selected cell equal to user entered value.
  # Called when the user presses the Enter key.

  def reset_to_original(self):
    '''
    need to check if board positions are auto filled in. tbh idk how to do that
    '''
    '''
    inside for loops, check if auto filled. if not, set to 0 (clear)
    '''
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        self.cells[i][j].value = self.generator[i][j]
        self.cells[i][j].temp = 0
        # setting up the sudoku board

  # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

  def is_full(self):

    for i in range(len(self.cells)):
      for j in range(len(self.cells[0])):
        if self.cells[i][j].value == 0:
          return False
    return True

  # Returns a Boolean value indicating whether the board is full or not.

  def find_empty(self):

    for i in range(len(self.cells)):
      for j in range(len(self.cells[0])):
        if self.cells[i][j] == 0:
          return (i, j)
    return None

  # Finds an empty cell and returns its row and col as a tuple (x, y).

  def check_board(self):
    for i in range(BOARD_SIZE):
      nums = [0 for a in range(BOARD_SIZE + 1)]
      for j in range(BOARD_SIZE):
        num = self.cells[i][j].value
        if nums[num] == 0:
          nums[num] = 1
        else:
          return False

    for i in range(BOARD_SIZE):
      nums = [0 for a in range(BOARD_SIZE + 1)]
      for j in range(BOARD_SIZE):
        num = self.cells[j][i].value
        if nums[num] == 0:
          nums[num] = 1
        else:
          return False

    for i in range(3):
      for j in range(3):
        nums = [0 for a in range(BOARD_SIZE + 1)]
        for k in range(i * 3, i * 3 + 3):
          for l in range(j * 3, j * 3 + 3):
            num = self.cells[k][l].value
            if nums[num] == 0:
              nums[num] = 1
            else:
              return False
    return True

    # for i in range(9):
    #   for j in range(9):
    #     for z in range(9):
    #     check1 = valid_in_col(i, self.cells[j][i].value)
    #     check2 = valid_in_row(j, self.cells[j][i].value)
    #     row_start = (j // 3) * 3
    #     col_start = (i // 3) * 3
    #     check3 = SudokuGenerator.valid_in_box(j, i, self.cells[j][i].value)

    #     if check1 is False or check2 is False or check3 is False:
    #         return False
    #     else:
    #         return True

  # Check whether the Sudoku board is solved correctly.
