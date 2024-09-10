# Code with Drex

import random

# Constants for the game board dimensions
ROWS = 3
COLS = 3

def display_board(board):
    """Displays the current game board"""
    print("\n#---#---#---#")
    for row in board:
        print("|", " | ".join(str(cell) for cell in row), "| ")
        print("#---#---#---#")

def modify_board(board, slot_number, marker):
    """Update the game board with the player's or computer's marker"""
    slot_number -= 1
    row, col = divmod(slot_number, COLS)
    board[row][col] = marker
    """
    2 // 3 = 0
    2 % 3 = 2
    8 // 3 = 2
    8 % 3 = 2
    """

def player_turn(board, possible_choices):
    """Handles the player's turn."""
    display_board(board)
    while True:
        try:
            choice = int(input("ENter your slot number (1-9): "))
            if choice in possible_choices:
                modify_board(board, choice, 'X')
                possible_choices.remove(choice)
                print(possible_choices)
                display_board(board)
                break
        except ValueError:
            print('Please enter a valid number.')

def computer_turn(board, possible_choices):
    """Handles the computer's turn."""
    choice = random.choice(possible_choices)
    print("\nCPU choice: ", choice)
    modify_board(board, choice, 'O')
    possible_choices.remove(choice)
    print(possible_choices)
    display_board(board)


def check_for_winner(board):
    """Check if there is a winner and returns the winner or None."""
    # Check rows, columns and diagonais for a winning combination
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2]: # loop through each row for a winning combination
            return board[i][0]
        if  board[0][i] == board[1][i] == board[2][i]: # loop through each col for a winning combination
            return board[0][i]
        
    # Diagonals winning combination
    if board[0][0] == board[1][1] == board[2][2]: 
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]: 
        return board[0][2]
    
    return None

def play_game():
    """Main game loop"""
    board = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]
    possible_choices = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
    turn_counter = 0

    while possible_choices:
        if turn_counter % 2 == 0:
            player_turn(board, possible_choices)
        else:
            computer_turn(board, possible_choices)

        winner = check_for_winner(board)
        if winner:
            display_board(board)
            return winner

        turn_counter += 1

    return None


if __name__ == "__main__":
    x_score = 0
    o_score = 0

    while True:
        winner = play_game()
        if winner == 'X':
            x_score += 1
            print('\nYou Won!')
        elif winner == 'O':
            o_score += 1
            print('\nYou Lost!')
        else:
            print("\nIt's a tie!")

        print(f"Current Score: You (X): {x_score} | CPU (O): {o_score}")

        replay = input("Do you want to play again? (Y/N): ").strip().lower()
        if replay != 'y':
            print('Thanks for playing')
            break


