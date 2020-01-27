
#Sudoku solver using backtracking algorithm
#from sudoku_GUI import Sudoku

class SudokuSolver:

    def __init__(self):
        pass

    def print_board(self, board):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" | ")
            print("\n", end="")

    def is_solved_place(self, board, position):
        # check if there's any unsolved place, also returns position
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    position[0], position[1] = i, j
                    return True
        return False

    def check_row(self, board, row, num):
        # check if there's a number in a row already
        for i in range(9):
            if board[row][i] == num:
                return True
        return False

    def check_col(self, board, col, num):
        # check if there's a number in a column already
        for i in range(9):
            if board[i][col] == num:
                return True
        return False

    def check_cube(self, board, row, col, num):
        # check if there's a number in a cube 3x3 already
        for i in range(3):
            for j in range(3):
                #print(board[row-row%3 + i][col-col%3 + j])
                if board[row + i][col + j] == num:
                    return True
        return False

    def check_all(self, board, row, col, num):
        return not self.check_col(board, col, num) and not self.check_row(board, row, num) \
               and not self.check_cube(board, row - row%3, col - col%3, num)


if __name__ == "__main__":

    sudoku_solver = SudokuSolver()


    # assigning values to the grid
    board = [[3,0,6,5,0,8,4,0,0],
             [5,2,0,0,0,0,0,0,0],
             [0,8,7,0,0,0,0,0,1],
             [0,0,3,0,1,0,0,8,0],
             [9,0,0,8,6,3,0,0,5],
             [0,5,0,0,9,0,6,0,0],
             [1,3,0,0,0,0,2,5,0],
             [0,0,0,0,0,0,0,7,4],
             [0,0,5,2,0,6,3,0,9]]

    if sudoku_solver.solve_sudoku(board):
        sudoku_solver.print_board(board)
    else:
        print("No solution exists")
