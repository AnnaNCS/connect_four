from main import str_to_board, print_board, has_connect_four, lowest_empty_row

def function_incorrect(board):
    print("FAIL on ")
    print_board(board)
    exit(1)

def main():

    # HAS_CONNECT_FOUR TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | _  _  _  _  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  O  X  _  _ |
    3  | _  _  O  X  X  O  X |
    4  | _  _  X  O  O  O  X |
    5  | _  X  X  O  O  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  _  _  _  _  _  O |
    2  | O  _  _  _  _  _  O |
    3  | O  _  _  _  _  _  O |
    4  | O  _  _  _  _  _  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    # LOWEST_EMPTY_ROW TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | _  _  _  _  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != 5:
        function_incorrect(board)

    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  O  O  O  O  O  O |
    2  | O  O  O  O  O  O  O |
    3  | O  O  O  O  O  O  O |
    4  | O  O  O  O  O  O  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != -1:
        function_incorrect(board)

    #More Testcases

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  O  _  X  _  _ |
    3  | _  _  X  X  O  X  _ |
    4  | _  _  X  O  O  O  X |
    5  | _  X  X  O  O  O  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  O  _  _  _  _  _ |
    3  | _  O  _  _  X  _  _ |
    4  | _  O  _  _  X  _  _ |
    5  | _  O  _  _  X  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  O  X  O  _  _  _ |
    3  | _  O  O  O  X  O  X |
    4  | X  O  X  X  O  X  X |
    5  | X  O  O  O  X  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | O  O  _  _  _  _  _ |
    3  | X  X  O  _  _  _  _ |
    4  | X  O  O  O  X  _  _ |
    5  | X  X  X  O  O  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | O  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | O  _  _  _  _  _  _ |
    5  | O  _  X  X  X  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')

    if has_connect_four(board):
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  O  _  _  O  X |
    1  | O  X  X  X  O  O  X |
    2  | O  X  O  X  X  X  O |
    3  | O  O  O  X  O  X  O |
    4  | X  X  X  O  X  O  O |
    5  | X  O  X  X  O  O  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 3) != 0:
        function_incorrect(board)

    board = str_to_board('''
     0  | _  _  _  _  _  _  _ |
     1  | _  _  _  _  _  _  O |
     2  | _  O  _  O  _  _  X |
     3  | X  X  X  O  X  O  X |
     4  | O  O  O  X  O  X  X |
     5  | O  X  O  O  X  X  O |
        +---------------------+
          0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 2) != 2:
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  X  _  _  _  _ |
    4  | O  _  X  _  X  _  O |
    5  | O  X  X  X  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 1) != 4:
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  O  X  _  _ |
    3  | _  _  O  X  X  O  X |
    4  | _  _  X  O  O  O  X |
    5  | _  X  X  O  O  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != 5:
        function_incorrect(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  X  _  _ |
    4  | _  _  _  _  O  _  _ |
    5  | _  _  X  O  O  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != 5:
        function_incorrect(board)

if __name__ == "__main__":
    print("Running the testcases...")
    main()
    print("Very succesfull run!")
