import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)

    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Cell already taken. Try again.")
                continue
        else:
            print("AI is making a move...")
            move = get_best_move(board)
            board[move[0]][move[1]] = 'O'

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
