"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
import copy
import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the duration
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # Return the original result
    return wrapper



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves=0 
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] in [X, O]:
                moves += 1 if board[y][x]==X else -1

    return X if not moves else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions={(i,j) for i in range(3) for j in range(3) if board[i][j]==EMPTY}
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('A very specific bad thing happened')
    action_board=copy.deepcopy(board)
    action_board[action[0]][action[1]]=player(board)
    return action_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board)==None:
        for y in range(len(board)):
            
            if None in board[y][:]:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (w:=winner(board)) in [X,O]:
        return 1 if w == X  else -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def minimax_value(board):
        if terminal(board):
            return utility(board)
        
        current_player = player(board)
        if current_player == X:
            return max(minimax_value(result(board, action)) for action in actions(board))
        else:
            return min(minimax_value(result(board, action)) for action in actions(board))
    
    if terminal(board):
        return None

    current_player = player(board)
    possible_actions = actions(board)

    # Get the optimal action based on the current player
    optimal_action = max(possible_actions, key=lambda action: minimax_value(result(board, action))) \
        if current_player == X else \
        min(possible_actions, key=lambda action: minimax_value(result(board, action)))
    
    return optimal_action
