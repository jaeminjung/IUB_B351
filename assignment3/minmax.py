import gamePlay
from copy import deepcopy

def maxvalue(board, color, a, b, level):
    v = -9999
    level -= 1
    moves = []

    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, color, (i, j)):
                moves.append((i, j))
    if len(moves) == 0:
        return "pass"

    color = gamePlay.opponent(color)
    for i in range(0, len(moves)):
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

def minvalue(board, color, a, b, level):
    v = +9999
    level -= 1
    moves = []

    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, color, (i, j)):
                moves.append((i, j))

    color = gamePlay.opponent(color)
    for i in range(0, len(moves)):
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

print(maxvalue([[" ,", " ,", " ,", " ,", " ,", " ,",  " ,",  " ,"],
                [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
                [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
                [" ,", " ,", " ,", "W", "B", " ,", " ,", " ,"],
                [" ,", " ,", " ,", "B", "W", " ,", " ,", " ,"],
                [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
                [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
                [" ,", " ,", " ,", " ,", " ,", " ,", " ,", " ,"],
                 ], "W", -9999, 9999, 0))
