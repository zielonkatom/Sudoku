

import pygame
from sudoku_solver import SudokuSolver
from math import floor
from tkinter import *
from tkinter import messagebox
import time

# define colors and screen sizes
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

WINDOWMULTIPLIER = 8

WINDOWHEIGHT = 90
WINDOWWIDTH = 90

FULLSIZE = (WINDOWHEIGHT*WINDOWMULTIPLIER, WINDOWWIDTH*WINDOWMULTIPLIER)

CUBESIZE = FULLSIZE[0] // 3
CELLSIZE = CUBESIZE // 3


class Sudoku:

    def __init__(self):

        pygame.init()
        self.sudoku_rules = SudokuSolver()
        self.size = FULLSIZE
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("SUDOKU")
        self.screen.fill(WHITE)
        self.draw_grid()

    def draw_grid(self):
        """Draw grid, scales with screen size"""

        for x in range(0, FULLSIZE[0], CELLSIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, FULLSIZE[0]))
        for y in range(0, FULLSIZE[1], CELLSIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (FULLSIZE[0], y))

        for x in range(0, FULLSIZE[0], CUBESIZE):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, FULLSIZE[0]), 2)
        for y in range(0, FULLSIZE[1], CUBESIZE):
            pygame.draw.line(self.screen, BLACK, (0, y), (FULLSIZE[0], y), 2)

    def fill_number(self, num, x, y):
        """Fill the grid with a num(ber) at x, y position"""
        self.font = pygame.font.SysFont(None, 70)
        # put new fresh text
        text = self.font.render(num, False, BLACK, None)
        text_rect = text.get_rect()
        # set the center of the rectangular object.
        text_rect.center = (x // 2 - CELLSIZE // 2, y // 2 - CELLSIZE // 2)

        # blank rectangle, to hide previous results
        pygame.draw.rect(self.screen, WHITE, (text_rect.left - 0.2 * CELLSIZE, text_rect.top,
                                            CELLSIZE - 0.3 * CELLSIZE, CELLSIZE - 0.3 * CELLSIZE))


        self.screen.blit(text, text_rect)

    def fill_grid(self, board):
        """Fill the whole grid calling fill_number function"""
        for x in range(CELLSIZE, FULLSIZE[0] + CELLSIZE, CELLSIZE):
            for y in range(CELLSIZE, FULLSIZE[0] + CELLSIZE, CELLSIZE):
                if str(board[(y // CELLSIZE - 1) % 9][(x // CELLSIZE - 1) % 9]) == "0":
                    self.fill_number(" ", x * 2, y * 2)
                else:
                    self.fill_number(str(board[(y // CELLSIZE - 1) % 9][(x // CELLSIZE - 1) % 9]), x*2, y*2)

    def solve_sudoku(self, board):
        """Backtracking algorithm"""

        position = [0, 0]

        # End game if there are not unsolved positions
        if not self.sudoku_rules.is_solved_place(board, position):
            return True

        for num in range(1, 10):
            if self.sudoku_rules.check_all(board, position[0], position[1], num):

                board[position[0]][position[1]] = num

                self.fill_grid(board)
                pygame.display.flip()

                if self.solve_sudoku(board):
                    return True

                board[position[0]][position[1]] = 0
                self.fill_grid(board)

                pygame.display.flip()

        return False

    def mouse_press_cell(self):
        """Get mouse position and highlight closest cell. Return x, y of the cell."""
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, WHITE, (floor(pos[0] / CELLSIZE) * CELLSIZE + 0.1 * CELLSIZE,
                                             floor(pos[1] / CELLSIZE) * CELLSIZE + 0.1 * CELLSIZE,
                                             CELLSIZE - 0.1 * CELLSIZE, CELLSIZE - 0.1 * CELLSIZE))

        x, y = floor(pos[1] / CELLSIZE), floor(pos[0] / CELLSIZE)

        return x, y

    def input_num(self, board, x, y):
        """Fill the cell with a number after clicking a mouse button"""
        wait_for_num = True

        while wait_for_num:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        board[x][y] = 0
                    if event.key == pygame.K_1:
                        if self.sudoku_rules.check_all(board, x, y, 1):
                            board[x][y] = 1
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_2:
                        if self.sudoku_rules.check_all(board, x, y, 2):
                            board[x][y] = 2
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_3:
                        if self.sudoku_rules.check_all(board, x, y, 3):
                            board[x][y] = 3
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_4:
                        if self.sudoku_rules.check_all(board, x, y, 4):
                            board[x][y] = 4
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_5:
                        if self.sudoku_rules.check_all(board, x, y, 5):
                            board[x][y] = 5
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_6:
                        if self.sudoku_rules.check_all(board, x, y, 6):
                            board[x][y] = 6
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_7:
                        if self.sudoku_rules.check_all(board, x, y, 7):
                            board[x][y] = 7
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_8:
                        if self.sudoku_rules.check_all(board, x, y, 8):
                            board[x][y] = 8
                        else:
                            print("Wrong move")
                    if event.key == pygame.K_9:
                        if self.sudoku_rules.check_all(board, x, y, 9):
                            board[x][y] = 9
                        else:
                            print("Wrong move")

                    wait_for_num = False

        self.fill_grid(board)


sudoku = Sudoku()

game_on = True
clock = pygame.time.Clock()

board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 0, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 9]]

fresh_board = board.copy()

# fill grid before the game starts
sudoku.fill_grid(board)

# Main loop
while game_on:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_on = False

        elif event.type == pygame.KEYDOWN:
            # Run backtracking algorithm if SPACE is pressed
            if event.key == pygame.K_SPACE:
                if sudoku.solve_sudoku(board):
                    sudoku.solve_sudoku(board)
                    Tk().wm_withdraw()  # to hide the main window
                    messagebox.showinfo('SUDOKU', 'Solved!')
                else:
                    print("No solution exists")
                    Tk().wm_withdraw()  # to hide the main window
                    messagebox.showinfo('SUDOKU', 'No solution exists!')

        elif event.type == pygame.MOUSEBUTTONUP:
            # On mouse button press get coords and run input num function
            x, y = sudoku.mouse_press_cell()
            sudoku.input_num(board, x, y)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
