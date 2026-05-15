# Global variables
board = []
nrows = 3
MAX_MOVES = nrows * nrows

players = ['X', 'O']
EMPTY = '.'


def initBoard():
    """Initialises (or resets) the board to all empty positions."""
    global board
    board = [[EMPTY for _ in range(nrows)] for _ in range(nrows)]


def showBoard():
    """Prints the current board state to the terminal."""
    for r in range(nrows):
        for c in range(nrows):
            print(" {}".format(board[r][c]), end='')
        print()


def checkMove(p):
    """
    Checks whether player p has a winning sequence on the board.

    Args:
        p (str): The player symbol ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    seq, tseq = False, True

    # Check rows
    for r in range(nrows):
        if seq:
            break
        tseq = True
        for c in range(nrows):
            if not tseq:
                break
            tseq = (board[r][c] == p)
        seq = tseq

    # Check columns
    if not seq:
        for c in range(nrows):
            if seq:
                break
            tseq = True
            for r in range(nrows):
                if not tseq:
                    break
                tseq = (board[r][c] == p)
            seq = tseq

    # Check main diagonal (top-left to bottom-right)
    if not seq:
        tseq = True
        for r in range(nrows):
            if not tseq:
                break
            tseq = (board[r][r] == p)
        seq = tseq

    # Check anti-diagonal (top-right to bottom-left)
    if not seq:
        tseq = True
        for r in range(nrows):
            if not tseq:
                break
            tseq = (board[r][nrows - r - 1] == p)
        seq = tseq

    return seq


def readMove():
    """
    Prompts the current player to enter a valid move.
    Validates range and checks the position is not already taken.

    Returns:
        tuple: (row, column) as 1-based integers.
    """
    x, y, done = 0, 0, False

    while not done:
        while True:
            try:
                y = int(input("Row: "))
                x = int(input("Column: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 1 <= y <= nrows and 1 <= x <= nrows:
                break
            print("Choose values between 1 and {}".format(nrows))

        if board[y - 1][x - 1] == EMPTY:
            done = True
        else:
            print("Position taken. Choose another position.")

    return y, x


def play():
    """Runs a single game of Tic-Tac-Toe until a win or draw."""
    current_player, total_moves = 0, 0

    initBoard()
    while True:
        p = players[current_player]
        showBoard()
        print("Player {} [{}]>".format(p, total_moves + 1))
        r, c = readMove()
        board[r - 1][c - 1] = p
        total_moves += 1

        if checkMove(p):
            showBoard()
            print("Player {} won in {} moves.".format(p, total_moves))
            break
        elif total_moves == MAX_MOVES:
            showBoard()
            print("Draw in {} moves.".format(total_moves))
            break

        current_player = (current_player + 1) % 2


def instructions():
    """Displays the game instructions."""
    print("TIC-TAC-TOE INSTRUCTIONS")
    print("========================")
    print("Player 1 (X) enters the row and column for each move.")
    print("Player 2 (O) plays after Player 1.")
    print("Players keep playing until there is a winner or a draw.")
    print()


def menu():
    """Displays the main menu."""
    print("TIC-TAC-TOE")
    print("===========")
    print("1-Instructions")
    print("2-Play")
    print("3-Quit")
    print()


def main():
    """Main loop — handles menu navigation."""
    while True:
        menu()
        try:
            n = int(input("Option: "))
        except ValueError:
            print("Invalid input. Please enter 1, 2 or 3.\n")
            continue

        if n == 1:
            instructions()
        elif n == 2:
            play()
        elif n == 3:
            print("Thanks for playing. Goodbye!")
            return
        else:
            print("Wrong option. Please choose 1, 2 or 3.\n")


if __name__ == "__main__":
    main()
