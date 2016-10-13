import gamePlay
from copy import deepcopy

#max-value algorithm
def maxvalue(board, color, a, b, level):
    v = -9999
    level -= 1
    moves = []

    #find the possible moves and append to moves
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, color, (i, j)):
                moves.append((i, j))
    if len(moves) == 0:
        return "pass"

    #change color and recursion to min-value algorithm
    color = gamePlay.opponent(color)
    for i in range(0, len(moves)):
        # if we go deep to level we sets, then return value of score
        if level == 0:
            if color == 'w' or 'W':
                v = gamePlay.score(board)[1]
            if color == 'b' or 'B':
                v = gamePlay.score(board)[0]
        else:
            v = max(v, minvalue(board, color, a, b, level))
        if v >= b:
            return v
        a = max(a, v)
    return v

#min-value algorithm
def minvalue(board, color, a, b, level):
    v = +9999
    level -= 1
    moves = []

    # find the possible moves and append to moves
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, color, (i, j)):
                moves.append((i, j))

    #color change and recursion to max-value algorithm
    color = gamePlay.opponent(color)
    for i in range(0, len(moves)):
        #if we go deep to level we sets, then return value of score
        if level == 0:
            if color == 'w' or 'W':
                v = gamePlay.score(board)[1]
            if color == 'b' or 'B':
                v = gamePlay.score(board)[0]
        else:
            v = min(v, maxvalue(board, color, a, b, level))
        if v <= b:
            return v
        b = min(b, v)
    return v

def nextMove(board, color):
    moves = []
    a = -9999
    b = 9999
    for i in range(8):
        for j in range(8):
            if valid(board, color, (i, j)):
                moves.append((i, j))
    if len(moves) == 0:
        return "pass"
    best = None

    #recursion to minvalue or maxvalue algorithm
    if color == "b" or "B":
        maxvalue(board, color, a, b, 5)
    if color == "w" or "W":
        minvalue(board, color, a, b, 5)

# print(gamePlay.score([[" ,", " ,", " ,", " ,", " ,", " ,",  " ,",  " ,"],
#                      [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", "W", "B", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", "B", "W", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                      [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                      ])[0])

# print(maxvalue([[" ,", " ,", " ,", " ,", " ,", " ,",  " ,",  " ,"],
#                 [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", "W", "B", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", "B", "W", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                 [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
#                  ], "W", -9999, 9999, 0))
