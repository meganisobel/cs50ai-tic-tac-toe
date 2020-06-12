"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

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
    takes board state
    return which players turn it is X or 0 
    in intial game state X gets the first move 
    any return value is acceptable if terminal board is provided as input

    """
    X_counter = 0 
    O_counter = 0
    for i in board:
        for j in i:
            if j == X:
                X_counter += 1
            if j == O:
                O_counter += 1

    if X_counter == 0 and O_counter == 0:
        return X
    elif  X_counter > O_counter:
        return O
    else:
        return X 
            
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0,1, or 2)
    j corresponds to which cell in the row 0, 1 or 2
    """
    actions = []   
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                thisTuple = (i, j)
                actions.append(thisTuple)
    
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    takse board and action as input and return a new board state without modifying the original board 

    if action not valid ation for the board your program should raise an exception 

    the returned board state should be the board that would result from taking the origibal input board 
    and letting the player whose turn it is make their move at the cell indicated by the input action 

    want to make a deep copy of the board first before making any changes 
    """

    i = action[0]
    j = action[1]
  

    nextPlayer = player(board)
    boardCopy = copy.deepcopy(board)

    boardCopy[i][j] = nextPlayer
    return boardCopy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.

    if X won return X if 0 won return 0 
    3 moves horizontally / vertically or diagonally 
    at most one winner 
    if no winner return None - game in progress or tie 
    """
    horzontialSummary = set()
    verticalSummary = set()

    backDiagonalSummary = [board[0][0], board[1][1], board[2][2]]
    forwardDiagonamSummary = [board[0][2], board[1][1], board[2][0]]
    row_1 = [board[0][0], board[0][1], board[0][2]]
    row_2 = [board[1][0], board[1][1], board[1][2]]
    row_3 = [board[2][0], board[2][1], board[2][2]]
    col_1 = [board[0][0], board[1][0], board[2][0]]
    col_2 = [board[0][1], board[1][1], board[2][1]]
    col_3 = [board[0][2], board[1][2], board[2][2]]

    X_wins = [X, X, X]
    O_wins = [O, O, O]

    possible_wins = [forwardDiagonamSummary, backDiagonalSummary, row_1, row_2, row_3, col_1, col_2, col_3] 

    for win in possible_wins: 
        if win == X_wins:
            return X
        elif win == O_wins:
            return O

    return None 

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    if over bc osomeone won or all cells filled return true 
    else false 
    """

    if winner(board) == X or winner(board) == O:
        return True
    
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    else:
        return True 

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    accept a terminal board as input and the output the utility of the board 

    if X has won utility 1 
    if 0 has won utility -1
    if tie 0 
    """
    output = winner(board)
    if output == X:
        return 1
    elif output == O:
        return -1
    elif output == None:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    return optimal move for the player to move on that board 
    optial actionm (i, j) - if multiple moves are equally optimal any acceptable 
    if board is terminal return none 
    """
    options_X = []
    options_O = []
    options_X.clear()
    options_O.clear()

    if terminal(board):
        return None

    nextPlayer = player(board)
    if nextPlayer == X:
        for action in actions(board):
            child = result(board, action)
            v = find_minimax(child, False)
            options_X.append([action, v])
        temp = -1000
        position = 0
        for i in range(len(options_X)):
            if options_X[i][1] > temp:
                temp = options_X[i][1]
                position = i 
        best_action = options_X[position][0]
        return best_action

    if nextPlayer == O:
        for action in actions(board):
            child = result(board, action)
            v = find_minimax(child, True)
            options_O.append([action, v])
        temp = 1000
        position = 0
        for i in range(len(options_O)):
            if options_O[i][1] < temp:
                temp = options_O[i][1]
                position = i 
        best_action = options_O[position][0]
        return best_action

    raise NotImplementedError



def find_minimax(board, maximisingPlayer):
    if terminal(board):
        return utility(board)
    if maximisingPlayer:
        bestVal = -1000
        for action in actions(board):
            value = find_minimax(result(board, action), False)
            bestVal = max(bestVal, value)
        return bestVal


    else:
        bestVal = 1000
        for action in actions(board): 
            value = find_minimax(result(board, action), True)
            bestVal = min(bestVal, value)
        return bestVal