import random

def display_board(board):
    """Displays the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def player_input():
    """Gets input from the player (X or O)."""
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, do you want to be X or O? ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """Places the marker on the board."""
    board[position // 3][position % 3] = marker

def win_check(board, mark):
    """Checks if a player has won."""
    return ((board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or  # across the top
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or  # across the middle
            (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or  # across the bottom
            (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or  # down the left side
            (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or  # down the middle
            (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or  # down the right side
            (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or  # diagonal
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark))  # diagonal

def choose_first():
    """Randomly chooses who goes first."""
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def space_check(board, position):
    """Checks if a space on the board is free."""
    return board[position // 3][position % 3] == ' '

def player_choice(board):
    """Gets the player's next move."""
    position = 0
    while position not in range(1, 10) or not space_check(board, position - 1):
        try:
            position = int(input("Choose a position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    return position - 1


def minimax(board, depth, maximizingPlayer):
    """Minimax algorithm for Tic-Tac-Toe."""
    if win_check(board, 'O'):  # Computer wins
        return 1
    elif win_check(board, 'X'):  # Player wins
        return -1
    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):  # It's a tie
        return 0

    if maximizingPlayer:
        maxEval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo the move (backtracking)
                    maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo the move (backtracking)
                    minEval = min(minEval, eval)
        return minEval

def find_best_move(board):
    """Finds the best move for the computer using Minimax."""
    bestVal = -float('inf')
    bestMove = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                moveVal = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move
                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = i * 3 + j
    return bestMove


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

# Main game loop
while True:
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_marker, computer_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player_marker, position)

            if win_check(board, player_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Computer'

        else:  # Computer's turn
            best_move = find_best_move(board)
            place_marker(board, computer_marker, best_move)

            if win_check(board, computer_marker):
                display_board(board)
                print('The computer has won!')
                game_on = False
            else:
                if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player'

    if not replay():
        break