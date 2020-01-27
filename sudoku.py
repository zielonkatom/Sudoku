
#Sudoku solver using backtracking algorithm

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" | ")
        print("\n", end="")

def is_solved_place(board, position):
    # check if there's any unsolved place, also returns position
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                position[0], position[1] = i, j
                return True
    return False

def check_row(board, row, num):
    # check if there's a number in a row already
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def check_col(board, col, num):
    # check if there's a number in a column already
    for i in range(9):
        if board[i][col] == num:
            return True
    return False

def check_cube(board, row, col, num):
    # check if there's a number in a cube 3x3 already
    for i in range(3):
        for j in range(3):
            #print(board[row-row%3 + i][col-col%3 + j])
            if board[row + i][col + j] == num:
                return True
    return False

def check_all(board, row, col, num):
    return not check_col(board, col, num) and not check_row(board, row, num) and not check_cube(board, row - row%3, col - col%3, num)

def solve_sudoku(board):

    position = [0, 0]

    # End game if there are not unsolved positions
    if not is_solved_place(board, position):
        return True

    for num in range(1, 10):
        if check_all(board, position[0], position[1], num):

            board[position[0]][position[1]] = num

            if solve_sudoku(board):
                return True

            board[position[0]][position[1]] = 0

    return False


if __name__ == "__main__":


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

    print(check_row(board, 0, 1))

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists")
