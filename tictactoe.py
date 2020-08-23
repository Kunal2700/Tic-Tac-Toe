"""
Tic Tac Toe Player
"""

import math, copy

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
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] != EMPTY:
        raise Exception

    new_board = copy.deepcopy(board)
    p = player(board)
    
    new_board[i][j] = p

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check Horizontal
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # Check Vertical
    column = []
    for i in range(len(board)):
        for j in range(len(board)):
            column.append(board[j][i])
        if column.count(X) == 3:
            return X
        elif column.count(O) == 3:
            return O
        column.clear()

    # Check Diagonal
    diag = []
    for i in range(len(board)):
        diag.append(board[i][i])
    if diag.count(X) == 3:
        return X
    elif diag.count(O) == 3:
        return O
    diag.clear()

    for i in range(len(board)):
        diag.append(board[i][3-i-1])
    if diag.count(X) == 3:
        return X
    elif diag.count(O) == 3:
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for row in board:
        for value in row:
            if value == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    AI = player(board)
    pairs = []
    options = set()

    if AI == O:
        for action in actions(board):
            pairs.append((action, max_value(result(board, action))))
        values = [pair[1] for pair in pairs]
        min_action = min(values)
        for pair in pairs:
            if pair[1] == min_action:
                options.add(pair[0])
    else:
        for action in actions(board):
            pairs.append((action, min_value(result(board, action))))
        values = [pair[1] for pair in pairs]
        max_action = max(values)
        for pair in pairs:
            if pair[1] == max_action:
                options.add(pair[0])
    
    return options.pop()


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
