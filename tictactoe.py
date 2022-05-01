''' Tic-Tac-Toe Assignment
    Author: John Lydiksen
'''

from operator import truediv


def main():
    player = next_player("")
    board = make_board()

    # while there is not a tie or a winner,
    # keep going through the players turns

    while (tie_game(board) or result_winner(board)) == False:
        display_board(board)
        player_action(player, board)
        player = next_player(player)
    display_board(board)
    if tie_game(board) == True:
        print('Tie Game. Thanks for playing!')
    else:
        print('Thanks for playing with me!')


def make_board():
    board = []

    for space in range(9):
        board.append(space + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# This function says whether or not the game is a tie or
# if there are still moves to be made
def tie_game(board):
    for space in range(9):
        if board[space] != "o" and board[space] != "x":
            return False
    return True



def result_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def player_action(player, board):
    space = int(input(f"{player}'s turn to make a move (1-9): "))
    board[space - 1] = player


def next_player(current):
    if current == "" or current == "x":
        return "o"
    elif current == "o":
        return "x"


if __name__ == "__main__":
    main()