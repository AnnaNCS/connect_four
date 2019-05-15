from textwrap import dedent

EMPTY = "_" # underscore
EX = "X" # capital x
OH = "O" # capital o

NUM_ROWS = 6
NUM_COLS = 7


def lowest_empty_row(board, col):
    i = 5
    while i >= 0:
        if board[i][col] == EMPTY:
            return i
        i -= 1
    return -1

def has_connect_four(board):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if c <= 3 and board[r][c] != EMPTY and board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                return True
            if r <= 2 and board[r][c] != EMPTY and board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                return True
            if r >= 3 and c <= 3 and board[r][c] != EMPTY and board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                return True
            if r >= 3 and c >= 3 and board[r][c] != EMPTY and board[r][c] == board[r-1][c-1] == board[r-2][c-2] == board[r-3][c-3]:
                return True
    else:
        return False

def get_input(board, player):
    col = input('Please drop your disc in a column: ')
    col = int(col)
    if lowest_empty_row(board, col) == -1:
        print('The board is full.')
    if col not in range(7):
        print("Out of range. Need to be a number between 0 and 6.")
    return col
    
def str_to_board(string):
   
    import re
    string = dedent(string).strip()
    board = []
    for line in string.splitlines():
        line = re.sub('[^_OX]', '', line)
        if not line:
            continue
        if len(line) != NUM_COLS:
            raise ValueError('Each row must have {} columns'.format(NUM_COLS))
        board.append(list(char for char in line))
    if len(board) != NUM_ROWS:
        raise ValueError('There must be {} rows'.format(NUM_ROWS))
    return board

def create_empty_board():
 
    board = []
    for row in range(NUM_ROWS):
        board.append(NUM_COLS * [EMPTY])
    return board


def print_salutation():

    print("Welcome!")
    print(dedent('''
    ##########################
    #        COMP 131        #
    #      CONNECT FOUR      #
    ##########################
    ''').strip())


def print_board(board):
  
    for i, row in enumerate(board):
        print(str(i) + '  | ' + '  '.join(col for col in row) + ' |')
    print('   +---------------------+')
    print('     0  1  2  3  4  5  6')


def print_valediction(num_empties, player):
   
    if num_empties == 0:
        text = 'A DRAW'
    elif player == EX:
        text = 'X WINS'
    else:
        text = 'O WINS'
    print(dedent('''
    ##########################
    #  !!!!   {}   !!!!  #
    ##########################
    '''.format(text)).strip())
    
def main():
    
    print_salutation()
    board = create_empty_board()
    player = EX
    has_win = False
    num_empties = NUM_ROWS * NUM_COLS
    while not has_win and num_empties:
        print()
        print_board(board)
        print()
        if player == EX:
            player = OH
        else:
            player = EX
        col = get_input(board, player)
        row = lowest_empty_row(board, col)
        board[row][col] = player
        has_win = has_connect_four(board)
        num_empties -= 1
    print()
    print_board(board)
    print()
    print_valediction(num_empties, player)

if __name__ == '__main__':
    main()
