import random
from copy import deepcopy

class gomoku:
    def __init__(self):
        self.board = [
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", "W", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","],
            [",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ",", ","]]

        self.simpleValue = [[1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2],
                            [1.2, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.2],
                            [1.2, 1.6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.2, 3.2, 3.2, 3.2, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 3.6, 3.6, 3.2, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 3.6, 3.2, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 3.6, 3.6, 3.2, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.2, 3.2, 3.2, 3.2, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2, 1.6, 1.2],
                            [1.2, 1.6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1.6, 1.2],
                            [1.2, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.2],
                            [1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2]]

        self.state_5_first_white = [[",", "W", "W", "W", "W"],
                                    ["W", "W", "W", "W", ","],
                                    ["W", "W", "W", ",", "W"],
                                    ["W", ",", "W", "W", "W"],
                                    ["W", "W", ",", "W", "W"]]
        self.state_5_first_black = [[",", "B", "B", "B", "B"],
                                  ["B", "B", "B", "B", ","],
                                  ["B", "B", "B", ",", "B"],
                                  ["B", ",", "B", "B", "B"],
                                  ["B", "B", ",", "B", "B"]]
        self.state_5_add_first = [[(0, 0)], [(0, 4)], [(0, 3)], [(0, 1)], [(0, 2)]]

        self.state_6_second_white = [[",", "W", "W", "W", ",", ","],
                                     [",", "W", "W", ",", "W", ","],
                                     [",", "W", ",", "W", "W", ","],
                                     [",", ",", "W", "W", "W", ","]]
        self.state_6_second_black = [[",", "B", "B", "B", ",", ","],
                                    [",", "B", "B", ",", "B", ","],
                                    [",", "B", ",", "B", "B", ","],
                                    [",", ",", "B", "B", "B", ","]]
        self.state_6_add_second = [[(0, 4)], [(0, 3)], [(0, 2)], [(0, 1)]]

        self.state_5_third_white = [[",", "W", "W", ",", ","],
                                    [",", "W", ",", "W", ","],
                                    [",", ",", "W", "W", ","]]
        self.state_5_third_black = [[",", "B", "B", ",", ","],
                                    [",", "B", ",", "B", ","],
                                    [",", ",", "B", "B", ","]]
        self.state_5_add_third = [[(0,3)], [(0,2)], [(0,1)]]

        self.state_5_fourth_white = [["W", "W", "W", ",", ","],
                                     ["W", "W", ",", "W", ","],
                                     ["W", "W", ",", ",", "W"],
                                     ["W", ",", "W", "W", ","],
                                     ["W", ",", "W", ",", "W"],
                                     ["W", ",", ",", "W", "W"],
                                     [",", "W", "W", "W", ","],
                                     [",", "W", "W", ",", "W"],
                                     [",", "W", ",", "W", "W"],
                                     [",", ",", "W", "W", "W"]]
        self.state_5_fourth_black = [["B", "B", "B", ",", ","],
                                  ["B", "B", ",", "B", ","],
                                  ["B", "B", ",", ",", "B"],
                                  ["B", ",", "B", "B", ","],
                                  ["B", ",", "B", ",", "B"],
                                  ["B", ",", ",", "B", "B"],
                                  [",", "B", "B", "B", ","],
                                  [",", "B", "B", ",", "B"],
                                  [",", "B", ",", "B", "B"],
                                  [",", ",", "B", "B", "B"]]
        self.state_5_add_fourth = [[(0, 3),(0,4)], [(0, 2), (0, 4)],
                                   [(0, 2), (0, 3)], [(0, 1), (0, 4)],
                                   [(0, 1), (0, 3)], [(0, 1), (0, 2)],
                                   [(0, 0), (0, 4)], [(0, 0), (0, 3)],
                                   [(0, 0), (0, 2)], [(0, 1),(0,0)]]

        self.state_4_fifth_white = [[",", "W", "W", ","],
                                    [",", "W", ",", "W"],
                                    ["W", ",", "W", ","]]
        self.state_4_fifth_black = [[",", "B", "B", ","],
                                    [",", "B", ",", "B"],
                                    ["B", ",", "B", ","]]
        self.state_4_add_fifth = [[(0,0), (0,3)],
                                  [(0,0), (0,2)],
                                  [(0,1), (0,3)]]
        self.state_4_sixth_white = [[",", "W", ",", ","],
                                    [",", ",", "W", ","]]
        self.state_4_sixth_black = [[",", ",", "B", ","],
                                    [",", "B", ",", ","]]
        self.state_4_add_sixth = [[(0,0), (0,2), (0,3)],
                                  [(0,0), (0,1), (0,4)]]
        self.state_5_sixth_white = [[",", "W", "W", ",", ","],
                                    [",", ",", "W", "W", ","],
                                    [",", "W", ",", "W", ","]]
        self.state_5_sixth_black = [[",", "B", "B", ",", ","],
                                    [",", ",", "B", "B", ","],
                                    [",", "B", ",", "B", ","]]
        self.state_5_add_sixth = [[(0,0), (0, 3), (0, 4)], [(0,0), (0,1), (0,4)], [(0,0), (0,2), (0,4)]]

    def printboard(self, board):
        print "    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14"
        context = ""
        for i in range(15):
            for j in range(15):
                if board[i][j] == "B":
                    context = context + "  " + "O"
                if board[i][j] == "W":
                    context = context + "  " + "X"
                if board[i][j] == ",":
                    context = context + "  " + u'\u2574'
            row = str(i)
            if i < 10:
                row = " " + str(i)
            print row + "" + context
            context = ""
        print "   "


    def validMove(self, board, coord):
        row = coord[0]
        col = coord[1]
        if row > 14 or col > 14 or row < 0 or col < 0:
            return False
        if board[row][col] != ",":
            return False
        return True

    def validmove(self, board, coord):
        row = coord[0]
        col = coord[1]
        if row > 14 or col > 14 or row < 0 or col < 0:
            return False
        if board[row][col] == ",":
            return True
        return False

    def endGameStatus(self, board, color):
        count = 0
        for i in range(15):
            for j in range(15):
                if board[i][j] == color:
                    count += 1
                else:
                    count = 0
                if count == 5:
                    return False
            count = 0
        count = 0
        for i in range(15):
            for j in range(15):
                if board[j][i] == color:
                    count += 1
                else:
                    count = 0
                if count == 5:
                    return False
            count = 0
        count = 0
        for i in range(15):
            for j in range(15):
                for k in range(5):
                    if i+k > 14 or j+k > 14:
                        break
                    if board[i+k][j+k] == color:
                        count += 1
                    else:
                        count = 0
                    if count == 5:
                        return False
                count = 0
                for l in range(5):
                    if i-l < 0 or j+l > 14:
                        break
                    if board[i-l][j+l] == color:
                        count += 1
                    else:
                        count = 0
                    if count == 5:
                        return False
                count = 0
        return True

    def randomMove(self, board):
        moves = []
        for i in range(15):
            for j in range(15):
                if board[i][j] == ",":
                    moves.append((i,j))
        #print moves
        if len(moves) == 0:
            return False
        move = moves[random.randint(0, len(moves)-1)]
        return move

    def makeMove(self, board, color, coord):
        board[int(coord[0])][int(coord[1])] = color
        self.printboard(board)

    def makeMove2(self, board, color, coord):
        board[int(coord[0])][int(coord[1])] = color
        return board

    def humanPlayer(self):
        validmove = False
        while not validmove:
            cord = raw_input("enter the coordinate(ex: 1,1) : ")
            cord = cord.split(",")
            rowcord = cord[0]
            colcord = cord[1]
            validmove = self.validMove(self.board, (int(rowcord), int(colcord)))
            if validmove == False:
                print "this is not valid move, try another one"
        return (rowcord, colcord)

    def playingGame(self):
        self.printboard(self.board)
        gameStatus = True
        while gameStatus:
            #human play
            self.makeMove(self.board, "B", self.humanPlayer())
            gameStatus = self.endGameStatus(self.board, "B")
            if gameStatus == False:
                print "you won!"
                break
            #AI play (random)
            #self.makeMove(self.board, "W", self.randomMove(self.board))

            #SimplePlay
            #self.makeMove(self.board, "W", self.simplePlay(self.board))

            #defenseAI
            #self.makeMove(self.board, "W", self.defenseAI(self.board, "B", 1))

            #findBestAI
            AImove = self.findstates(self.board, "W")
            self.makeMove(self.board, "W", AImove)
            print "Ai plays : " + str(AImove)
            gameStatus = self.endGameStatus(self.board, "W")

            if gameStatus == False:
                print "you lose!"
                break
        print "game over, restart it"
    ################################################
    ####################simplePlay
    def simplePlay(self, board):
        board = deepcopy(self.board)
        for i in range(15):
            for j in range(15):
                if board[i][j] == "B":
                    boundaries = self.findboundary((i,j))
                    for k in range(len(boundaries)):
                        self.simpleValue[boundaries[k][0]][boundaries[k][1]] += 2
                if board[i][j] == "W":
                    boundaries = self.findboundary((i, j))
                    for l in range(len(boundaries)):
                        self.simpleValue[boundaries[l][0]][boundaries[l][1]] += 2

        moves = []
        for i in range(15):
            for j in range(15):
                if self.board[i][j] == ",":
                    moves.append((i, j))
        if len(moves) == 0:
            return False

        bestmoves = moves[0]
        for i in range(len(moves)):
            if self.simpleValue[moves[i][0]][moves[i][1]] >= self.simpleValue[bestmoves[0]][bestmoves[1]]:
                bestmoves = moves[i]
        return bestmoves

    def findboundary(self,coord):
        row = coord[0]
        col = coord[1]
        possible_boundary = []
        if ((row == 0) or (row == 14)) and ((col == 0) or (col == 14)):
            if row == 0 and col == 0:
                possible_boundary.append((0, 1))
                possible_boundary.append((1, 0))
                possible_boundary.append((1, 1))
            if row == 0 and col == 14:
                possible_boundary.append((0, 13))
                possible_boundary.append((1, 13))
                possible_boundary.append((1, 14))
            if row == 14 and col == 0:
                possible_boundary.append((13, 0))
                possible_boundary.append((13, 1))
                possible_boundary.append((14, 1))
            if row == 14 and col == 14:
                possible_boundary.append((13, 13))
                possible_boundary.append((13, 14))
                possible_boundary.append((14, 13))
            return possible_boundary
        if row == 0 or row == 14 or col == 0 or col == 14:
            for i in range(2):
                for k in range(-1, 2):
                    if not ((i == 0) and (k == 0)):
                        # and (row+k > 14) and (row+i > 14) and (col+k > 14) and (col + i > 14)
                        if row == 0:
                            possible_boundary.append((row + i, col + k))
                        if row == 14:
                            possible_boundary.append((row - i, col + k))
                        if col == 0:
                            possible_boundary.append((row + k, col + i))
                        if col == 14:
                            possible_boundary.append((row + k, col - i))
            return possible_boundary
        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (i == 0 and j == 0):
                        possible_boundary.append((int(row) + i, int(col) + j))
            return possible_boundary
#####################################################
####################################################
    ## upgrade AI
    def findstates(self, board, color):
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"
        board = deepcopy(self.board)
        board2 = deepcopy(self.board)

        possiblemoves1_white = self.findstates_helper(board, self.state_5_first_white, self.state_5_add_first, 5)
        possiblemoves2_white = self.findstates_helper(board, self.state_6_second_white, self.state_6_add_second, 6)
        possiblemoves3_white = self.getpoints2(board, "W")
        #combine fourth  priority
        possiblemoves35_white = self.findstates_helper(board, self.state_5_third_white, self.state_5_add_third, 5)
        possiblemoves45_white = self.findstates_helper(board, self.state_5_fourth_white, self.state_5_add_fourth, 5)
        possiblemoves4_white = possiblemoves35_white + possiblemoves45_white
        possiblemoves5_white = self.findstates_helper(board, self.state_4_fifth_white, self.state_4_add_fifth, 4)
        possiblemoves6_white = self.findstates_helper(board, self.state_4_sixth_white,self.state_4_add_sixth, 4)
        possiblemoves7_white = self.findstates_helper(board, self.state_5_sixth_white, self.state_5_add_sixth, 5)

        possiblemoves1_black = self.findstates_helper(board, self.state_5_first_black, self.state_5_add_first, 5)
        possiblemoves2_black = self.findstates_helper(board, self.state_6_second_black, self.state_6_add_second, 6)
        possiblemoves3_black = self.getpoints2(board, "B")
        possiblemoves35_black = self.findstates_helper(board, self.state_5_third_black, self.state_5_add_third, 5)
        possiblemoves45_black = self.findstates_helper(board, self.state_5_fourth_black, self.state_5_add_fourth, 5)
        possiblemoves4_black = possiblemoves35_black + possiblemoves45_black
        possiblemoves5_black = self.findstates_helper(board, self.state_4_fifth_black, self.state_4_add_fifth, 4)
        possiblemoves6_black = self.findstates_helper(board, self.state_4_sixth_black, self.state_4_add_sixth, 4)
        possiblemoves7_black = self.findstates_helper(board, self.state_5_sixth_black, self.state_5_add_sixth, 5)
        # print str(len(possiblemoves1_white)) + "" + "  possiblemoves1_white", possiblemoves1_white
        # print str(len(possiblemoves2_white)) + "" + "  possiblemoves2_white", possiblemoves2_white
        # print str(len(possiblemoves3_white)) + "" + "  possiblemoves3_white", possiblemoves3_white
        # print str(len(possiblemoves4_white)) + "" + "  possiblemoves4_white", possiblemoves4_white
        # print str(len(possiblemoves5_white)) + "" + "  possiblemoves5_white", possiblemoves5_white
        # print str(len(possiblemoves6_white)) + "" + "  possiblemoves6_white", possiblemoves6_white
        # print str(len(possiblemoves7_white)) + "" + "  possiblemoves7_white", possiblemoves7_white
        # print str(len(possiblemoves1_black)) + "" + "  possiblemoves1_black"
        # print str(len(possiblemoves2_black)) + "" + "  possiblemoves2_black"
        # print str(len(possiblemoves3_black)) + "" + "  possiblemoves3_black"
        # print str(len(possiblemoves4_black)) + "" + "  possiblemoves4_black"
        # print str(len(possiblemoves5_black)) + "" + "  possiblemoves5_black"
        # print str(len(possiblemoves6_black)) + "" + "  possiblemoves6_black"

        if len(possiblemoves1_white) != 0:
            return possiblemoves1_white[random.randint(0, len(possiblemoves1_white)-1)]
        if len(possiblemoves1_black) != 0:
            return possiblemoves1_black[random.randint(0, len(possiblemoves1_black)-1)]
        if len(possiblemoves2_white) != 0:
            return possiblemoves2_white[random.randint(0, len(possiblemoves2_white)-1)]
        # if len(possiblemoves2_black) != 0:
        #     return possiblemoves2_black[random.randint(0, len(possiblemoves2_black)-1)]

        seeAhead = []
        before_sorting = [possiblemoves1_white, possiblemoves1_black, possiblemoves2_white, possiblemoves2_black,
                          possiblemoves3_white, possiblemoves3_black, possiblemoves4_white, possiblemoves4_black,
                          possiblemoves5_white, possiblemoves5_black, possiblemoves6_white, possiblemoves6_black,
                          possiblemoves7_white, possiblemoves7_black]
        for i in range(len(before_sorting)):
            pickfirst = before_sorting[i]
            for j in range(len(pickfirst)):
                if self.nonOverlap(seeAhead, pickfirst[j]):
                    if len(seeAhead) < 10:
                        seeAhead.append(pickfirst[j])

        print seeAhead
        valuelist = []
        for i in range(len(seeAhead)):
            valuelist.append(self.counteachPrioirty(self.makeMove2(board2, "W", (seeAhead[i])), "W"))
            board2 = deepcopy(self.board)
        highest_idx = 0
        highest = -999999
        print valuelist
        for i in range(len(valuelist)):
            if valuelist[i] >= highest:
                highest = valuelist[i]
                highest_idx = i
        return seeAhead[highest_idx]

        if len(possiblemoves3_white) != 0:
            return possiblemoves3_white[random.randint(0, len(possiblemoves3_white)-1)]
        if len(possiblemoves3_black) != 0:
            return possiblemoves3_black[random.randint(0, len(possiblemoves3_black)-1)]


        # if len(possiblemoves4_white) != 0:
        #     return possiblemoves4_white[random.randint(0, len(possiblemoves4_white)-1)]
        # if len(possiblemoves4_black) != 0:
        #     return possiblemoves4_black[random.randint(0, len(possiblemoves4_black)-1)]
        #
        # if len(possiblemoves5_white) != 0:
        #     return possiblemoves5_white[random.randint(0, len(possiblemoves5_white)-1)]
        # if len(possiblemoves5_black) != 0:
        #     return possiblemoves5_black[random.randint(0, len(possiblemoves5_black)-1)]
        #
        # if len(possiblemoves6_white) != 0:
        #     return possiblemoves6_white[random.randint(0, len(possiblemoves6_white)-1)]
        # if len(possiblemoves6_black) != 0:
        #     return possiblemoves6_black[random.randint(0, len(possiblemoves6_black)-1)]
        # seeAhead =[]
        # before_sorting = [possiblemoves4_white, possiblemoves4_black, possiblemoves5_white, possiblemoves5_black]
        # for i in range(len(before_sorting)):
        #     pickfirst = before_sorting[i]
        #     for j in range(len(pickfirst)):
        #         if self.nonOverlap(seeAhead, pickfirst[j]):
        #             seeAhead.append(pickfirst[j])
        #
        # if len(seeAhead) == 0:
        #     return self.simplePlay(board)
        # print seeAhead
        # valuelist = []
        # for i in range(len(seeAhead)):
        #     valuelist.append(self.counteachPrioirty(self.makeMove2(board2, "W", (seeAhead[i])), "W"))
        #     board2 = deepcopy(self.board)
        # highest_idx = 0
        # highest = -9999
        # print valuelist
        # for i in range(len(valuelist)):
        #     if valuelist[i] >= highest:
        #         highest = valuelist[i]
        #         highest_idx = i
        return seeAhead[highest_idx]


    def nonOverlap(self, array, value):
        arr_len = len(array)
        for i in range(arr_len):
            if array[i] == value:
                return False
        return True

    def findstates_helper(self, board, state_for_x, state_x_add, state_length):
        ans = []
        compare = []
        for i in range(15):
            for j in range(15):
                for k in range(state_length):
                    if j + k > 14:
                        break
                    else:
                        compare.append(board[i][j+k])
                for l in range(len(state_for_x)):
                    if state_for_x[l] == compare:
                        for m in range(len(state_x_add[l])):
                            if self.validmove(board, (i+ state_x_add[l][m][0], j+state_x_add[l][m][1])):
                                if self.nonOverlap(ans, (i+ state_x_add[l][m][0], j+state_x_add[l][m][1])):
                                    ans.append((i+ state_x_add[l][m][0], j+state_x_add[l][m][1]))

                compare = []
                for k in range(state_length):
                    if j + k > 14:
                        break
                    else:
                        compare.append(board[j+k][i])
                for l in range(len(state_for_x)):
                    if state_for_x[l] == compare:
                        for m in range(len(state_x_add[l])):
                            if self.validmove(board, (j + state_x_add[l][m][1], i + state_x_add[l][m][0])):
                                if self.nonOverlap(ans, (j + state_x_add[l][m][1], i + state_x_add[l][m][0])):
                                    ans.append((j + state_x_add[l][m][1], i + state_x_add[l][m][0]))

                compare = []
                for k in range(state_length):
                    if i + k > 14 or j + k > 14:
                        break
                    else:
                        compare.append(board[i+k][j+k])
                for l in range(len(state_for_x)):
                    if state_for_x[l] == compare:
                        for m in range(len(state_x_add[l])):
                            if self.validmove(board, (i + state_x_add[l][m][1], j + state_x_add[l][m][1])):
                                if self.nonOverlap(ans, (i + state_x_add[l][m][1], j + state_x_add[l][m][1])):
                                    ans.append((i + state_x_add[l][m][1], j + state_x_add[l][m][1]))

                compare = []
                for k in range(state_length):
                    if i + k > 14 or j - k < 0:
                        break
                    else:
                        compare.append(board[i+k][j-k])
                for l in range(len(state_for_x)):
                    if state_for_x[l] == compare:
                        for m in range(len(state_x_add[l])):
                            if self.validmove(board, (i + state_x_add[l][m][1], j - state_x_add[l][m][1])):
                                if self.nonOverlap(ans, (i + state_x_add[l][m][1], j - state_x_add[l][m][1])):
                                    ans.append((i + state_x_add[l][m][1], j - state_x_add[l][m][1]))
                compare = []
        return ans

    def evalfunction(self, color):
        board = self.board
        simpleValue = deepcopy(self.simpleValue)
        # print board
        # print simpleValue
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"

        for i in range(15):
            for j in range(15):
                if board[i][j] == color:
                    for k in range(5):
                        for l in range(5):
                            if 0 <= i-2+k < 15 and 0 <= j-2+l < 15:
                                if k == 0 or l == 0:
                                    simpleValue[i-2+k][j-2+l] += 1.5
                                else:
                                    simpleValue[i-2+k][j-2+l] += 2.5
                if board[i][j] == color_opp:
                    for k in range(5):
                        for l in range(5):
                            if 0 <= i-2+k < 15 and 0 <= j-2+l < 15:
                                if k == 0 or l == 0:
                                    simpleValue[i-2+k][j-2+l] -= 1.5
                                else:
                                    simpleValue[i-2+k][j-2+l] -= 2.5

        result = self.eachPriority("W")
        possiblemoves_white = result[0]
        possiblemoves_black = result[1]
        # print possiblemoves_white
        # print possiblemoves_black
        # print len(possiblemoves_black)

        for i in range(len(possiblemoves_white)):
            eachstate = possiblemoves_white[i]
            eachstate1 = possiblemoves_black[i]
            for j in range(len(eachstate)):
                if i == 4:
                    simpleValue[eachstate[j][0]][eachstate[j][1]] += 3
                else:
                    simpleValue[eachstate[j][0]][eachstate[j][1]] += 10**(4-i)
            for j in range(len(eachstate1)):
                if i == 4:
                    simpleValue[eachstate1[j][0]][eachstate1[j][1]] += 3
                else:
                    simpleValue[eachstate1[j][0]][eachstate1[j][1]] += 10 ** (4 - i)

        for i in range(15):
            for j in range(15):
                if board[i][j] == color or board[i][j] == color_opp:
                    simpleValue[i][j] = -99
        return simpleValue

    def counteachPrioirty(self, board, color):
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"
        value_color  = 0
        value_color_opp = 0

        possiblemoves1_white = self.findstates_helper(board, self.state_5_first_white, self.state_5_add_first, 5)
        possiblemoves2_white = self.findstates_helper(board, self.state_6_second_white, self.state_6_add_second, 6)
        possiblemoves3_white = self.getpoints2(board, "W")
        # combine fourth  priority
        possiblemoves35_white = self.findstates_helper(board, self.state_5_third_white, self.state_5_add_third, 5)
        possiblemoves45_white = self.findstates_helper(board, self.state_5_fourth_white, self.state_5_add_fourth, 5)
        possiblemoves4_white = possiblemoves35_white + possiblemoves45_white
        possiblemoves5_white = self.findstates_helper(board, self.state_4_fifth_white, self.state_4_add_fifth, 4)
        possiblemoves6_white = self.findstates_helper(board, self.state_4_sixth_white, self.state_4_add_sixth, 4)
        possiblemoves7_white = self.findstates_helper(board, self.state_5_sixth_white, self.state_5_add_sixth, 5)

        possiblemoves_white = [possiblemoves1_white, possiblemoves2_white, possiblemoves3_white, possiblemoves4_white,
                               possiblemoves5_white, possiblemoves6_white, possiblemoves7_white]

        for i in range(len(possiblemoves_white)):
            if i > 5:
                exp = 5
            else:
                exp = i
            value_color += len(possiblemoves_white[i]) * (20**(5-exp)) + 1

        possiblemoves1_black = self.findstates_helper(board, self.state_5_first_black, self.state_5_add_first, 5)
        possiblemoves2_black = self.findstates_helper(board, self.state_6_second_black, self.state_6_add_second, 6)
        possiblemoves3_black = self.getpoints2(board, "B")
        possiblemoves35_black = self.findstates_helper(board, self.state_5_third_black, self.state_5_add_third, 5)
        possiblemoves45_black = self.findstates_helper(board, self.state_5_fourth_black, self.state_5_add_fourth, 5)
        possiblemoves4_black = possiblemoves35_black + possiblemoves45_black
        possiblemoves5_black = self.findstates_helper(board, self.state_4_fifth_black, self.state_4_add_fifth, 4)
        possiblemoves6_black = self.findstates_helper(board, self.state_4_sixth_black, self.state_4_add_sixth, 4)
        possiblemoves7_black = self.findstates_helper(board, self.state_5_sixth_black, self.state_5_add_sixth, 5)
        possiblemoves_black = [possiblemoves1_black, possiblemoves2_black, possiblemoves3_black, possiblemoves4_black,
                               possiblemoves5_black, possiblemoves6_black, possiblemoves7_black]

        for i in range(len(possiblemoves_black)):
            if i > 5:
                exp1 = 5
            else:
                exp1 = i
            value_color_opp += len(possiblemoves_black[i]) * (20**((5-exp1)+1)) + 1

        if color == "W":
            return value_color - value_color_opp
        else:
            return value_color_opp - value_color

    def eachPriority(self, color):
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"

        board = deepcopy(self.board)
        possiblemoves1_white = self.findstates_helper(board, self.state_5_first_white, self.state_5_add_first, 5)
        possiblemoves2_white = self.findstates_helper(board, self.state_6_second_white, self.state_6_add_second, 6)
        possiblemoves3_white = self.getpoints2("W")
        # combine fourth  priority
        possiblemoves35_white = self.findstates_helper(board, self.state_5_third_white, self.state_5_add_third, 5)
        possiblemoves45_white = self.findstates_helper(board, self.state_5_fourth_white, self.state_5_add_fourth, 5)
        possiblemoves4_white = possiblemoves35_white + possiblemoves45_white
        possiblemoves5_white = self.findstates_helper(board, self.state_4_fifth_white, self.state_4_add_fifth, 4)

        #combine all priority
        possiblemoves_white = []
        possiblemoves_white.append(possiblemoves1_white)
        possiblemoves_white.append(possiblemoves2_white)
        possiblemoves_white.append(possiblemoves3_white)
        possiblemoves_white.append(possiblemoves4_white)
        possiblemoves_white.append(possiblemoves5_white)

        possiblemoves1_black = self.findstates_helper(board, self.state_5_first_black, self.state_5_add_first, 5)
        possiblemoves2_black = self.findstates_helper(board, self.state_6_second_black, self.state_6_add_second, 6)
        possiblemoves3_black = self.getpoints2("B")
        possiblemoves35_black = self.findstates_helper(board, self.state_5_third_black, self.state_5_add_third, 5)
        possiblemoves45_black = self.findstates_helper(board, self.state_5_fourth_black, self.state_5_add_fourth, 5)
        possiblemoves4_black = possiblemoves35_black + possiblemoves45_black
        possiblemoves5_black = self.findstates_helper(board, self.state_4_fifth_black, self.state_4_add_fifth, 4)

        possiblemoves_black = []
        possiblemoves_black.append(possiblemoves1_black)
        possiblemoves_black.append(possiblemoves2_black)
        possiblemoves_black.append(possiblemoves3_black)
        possiblemoves_black.append(possiblemoves4_black)
        possiblemoves_black.append(possiblemoves5_black)

        return possiblemoves_white, possiblemoves_black

    def getpossible(self, number, a, b):

        setpoint1 = [(a, b)]
        v_points1 = [(a, b - 1), (a, b + 3)]
        arrow_points1 = [(a, b + 4)]
        o_points1 = [(a, b + 1), (a, b + 2)]
        possible1 = [setpoint1, v_points1, arrow_points1, o_points1]

        setpoint2 = [(a, b)]
        v_points2 = [(a - 1, b - 1), (a + 3, b + 3)]
        arrow_points2 = [(a + 4, b + 4)]
        o_points2 = [(a + 1, b + 1), (a + 2, b + 2)]
        possible2 = [setpoint2, v_points2, arrow_points2, o_points2]

        setpoint3 = [(a, b)]
        v_points3 = [(a-1, b), (a+3, b)]
        arrow_points3 = [(a+4, b)]
        o_points3 = [(a+1, b), (a+2, b)]
        possible3 = [setpoint3, v_points3, arrow_points3, o_points3]

        setpoint4 = [(a, b)]
        v_points4 = [(a-1, b+1), (a+3, b-3)]
        arrow_points4 = [(a+4, b-4)]
        o_points4 = [(a+1, b-1), (a+2, b-2)]
        possible4 = [setpoint4, v_points4, arrow_points4, o_points4]

        setpoint1_180 = [(a,b)]
        v_points1_180 = [(a, b+1), (a, b-3)]
        arrow_points1_180 = [(a, b-4)]
        o_points1_180 = [(a, b-1), (a, b-2)]
        possible1_180 = [setpoint1_180, v_points1_180, arrow_points1_180, o_points1_180]

        setpoint5 = [(a, b)]
        v_points5 = [(a+1, b+1), (a-3, b-3)]
        arrow_points5 = [(a-4, b-4)]
        o_points5 = [(a-1, b-1), (a-2, b-2)]
        possible5 = [setpoint5, v_points5, arrow_points5, o_points5]

        setpoint6 = [(a, b)]
        v_points6 = [(a+1, b), (a-3, b)]
        arrow_points6 = [(a-4, b)]
        o_points6 = [(a-1,b), (a-2, b)]
        possible6 = [setpoint6, v_points6, arrow_points6, o_points6]

        setpoint7 = [(a, b)]
        v_points7 = [(a+1, b-1), (a-3, b+3)]
        arrow_points7 = [(a-4, b+4)]
        o_points7 = [(a-1, b+1), (a-2, b+2)]
        possible7 = [setpoint7, v_points7, arrow_points7, o_points7]

###########################################################################
        setpoint8 = [(a, b)]
        v_points8 = [(a, b-1), (a, b+2), (a, b+4)]
        arrow_points8 =[]
        o_points8 = [(a, b+1), (a, b+3)]
        possible8 = [setpoint8, v_points8, arrow_points8, o_points8]

        setpoint9 = [(a, b)]
        v_points9 = [(a-1, b-1), (a+2, b+2), (a+4, b+4)]
        arrow_points9 = []
        o_points9 = [(a+1, b+1), (a+3, b+3)]
        possible9 = [setpoint9, v_points9, arrow_points9, o_points9]

        setpoint10 = [(a, b)]
        v_points10 = [(a-1, b), (a+2, b), (a+4, b)]
        arrow_points10 = []
        o_points10 = [(a+1, b), (a+3, b)]
        possible10 = [setpoint10, v_points10, arrow_points10, o_points10]

        setpoint11 = [(a, b)]
        v_points11 = [(a-1, b+1), (a+2, b-2), (a+4, b-4)]
        arrow_points11 =[]
        o_points11 =[(a+1, b-1), (a+3, b-3)]
        possible11 = [setpoint11, v_points11, arrow_points11, o_points11]

        setpoint2_180 = [(a,b)]
        v_points2_180 = [(a, b+1), (a, b-2), (a, b-4)]
        arrow_points2_180 = []
        o_points2_180 = [(a, b-1), (a, b-3)]
        possible2_180 = [setpoint2_180, v_points2_180, arrow_points2_180, o_points2_180]

        setpoint12 = [(a, b)]
        v_points12 = [(a+1, b+1), (a-2, b-2), (a-4, b-4)]
        arrow_points12 = []
        o_points12 = [(a-1, b-1), (a-3, b-3)]
        possible12 = [setpoint12, v_points12, arrow_points12, o_points12]

        setpoint13 = [(a, b)]
        v_points13 = [(a+1, b), (a-2, b), (a-4, b)]
        arrow_points13 = []
        o_points13 = [(a-1, b), (a-3, b)]
        possible13 = [setpoint13, v_points13, arrow_points13, o_points13]

        setpoint14 = [(a, b)]
        v_points14 = [(a+1, b-1), (a-2, b+2), (a-4, b+4)]
        arrow_points14 =[]
        o_points14 = [(a-1, b+1), (a-3, b+3)]
        possible14 = [setpoint14, v_points14, arrow_points14, o_points14]

        ###############33333#################################3
        setpoint15 = [(a, b)]
        v_points15 = [(a, b-1), (a, b+1), (a, b+4)]
        arrow_points15 = []
        o_points15 = [(a, b+2), (a, b+3)]
        possible15 = [setpoint15, v_points15, arrow_points15, o_points15]

        setpoint16 = [(a, b)]
        v_points16 = [(a-1, b-1), (a+1, b+1), (a+4, b+4)]
        arrow_points16 = []
        o_points16 = [(a+2, b+2), (a+3, b+3)]
        possible16 = [setpoint16, v_points16, arrow_points16, o_points16]

        setpoint17 = [(a, b)]
        v_points17 = [(a-1, b), (a+1, b), (a+4, b)]
        arrow_points17 = []
        o_points17 = [(a+2, b), (a+3, b)]
        possible17 = [setpoint17, v_points17, arrow_points17, o_points17]

        setpoint18 = [(a, b)]
        v_points18 = [(a-1, b+1), (a+1, b-1), (a+4, b-4)]
        arrow_points18 = []
        o_points18 = [(a+2, b-2), (a+3, b-3)]
        possible18 = [setpoint18, v_points18, arrow_points18, o_points18]

        setpoint3_180 = [(a,b)]
        v_points3_180 = [(a,b+1), (a, b-1), (a, b-4)]
        arrow_points3_180 = []
        o_points3_180 = [(a, b-2), (a, b-3)]
        possible3_180 = [setpoint3_180, v_points3_180, arrow_points3_180, o_points3_180]

        setpoint19 = [(a, b)]
        v_points19 = [(a+1, b+1), (a-1, b-1), (a-4, b-4)]
        arrow_points19 = []
        o_points19 = [(a-2, b-2), (a-3, b-3)]
        possible19 = [setpoint19, v_points19, arrow_points19, o_points19]

        setpoint20 = [(a, b)]
        v_points20 = [(a+1, b), (a-1, b), (a-4, b)]
        arrow_points20 = []
        o_points20 = [(a-2, b), (a-3, b)]
        possible20 = [setpoint20, v_points20, arrow_points20, o_points20]

        setpoint21 = [(a, b)]
        v_points21 = [(a+1, b-1), (a-1, b+1), (a-4, b+4)]
        arrow_points21 = []
        o_points21 = [(a-2, b+2), (a-3, b+3)]
        possible21 = [setpoint21, v_points21, arrow_points21, o_points21]

###############################4444
        setpoint22 = [(a, b)]
        v_points22 = [(a, b-2), (a, b+2)]
        arrow_points22 = [(a, b+3)]
        o_points22 = [(a, b-1), (a, b+1)]
        possible22 = [setpoint22, v_points22, arrow_points22, o_points22]

        setpoint23 = [(a, b)]
        v_points23 = [(a-2, b-2), (a+2, b+2)]
        arrow_points23 = [(a+3, b+3)]
        o_points23 = [(a-1, b-1), (a+1, b+1)]
        possible23 = [setpoint23, v_points23, arrow_points23, o_points23]

        setpoint24 = [(a, b)]
        v_points24 = [(a-2, b), (a+2, b)]
        arrow_points24 = [(a+3, b)]
        o_points24 = [(a+1, b), (a-1, b)]
        possible24 = [setpoint24, v_points24, arrow_points24, o_points24]

        setpoint25 = [(a, b)]
        v_points25 = [(a-2, b+2), (a+2, b-2)]
        arrow_points25 = [(a+3, b-3)]
        o_points25 = [(a+1, b-1), (a-1, b+1)]
        possible25 = [setpoint25, v_points25, arrow_points25, o_points25]

        setpoint4_180 = [(a,b)]
        v_points4_180 = [(a, b+2), (a, b-2)]
        arrow_points4_180 = [(a, b-3)]
        o_points4_180 = [(a, b+1), (a, b-1)]
        possible4_180 = [setpoint4_180, v_points4_180, arrow_points4_180, o_points4_180]

        setpoint26 = [(a, b)]
        v_points26 = [(a+2, b+2), (a-2, b-2)]
        arrow_points26 = [(a-3, b-3)]
        o_points26 = [(a+1, b+1), (a-1, b-1)]
        possible26 = [setpoint26, v_points26, arrow_points26, o_points26]

        setpoint27 = [(a, b)]
        v_points27 = [(a-2, b), (a+2, b)]
        arrow_points27 = [(a-3, b)]
        o_points27 = [(a-1, b), (a+1, b)]
        possible27 = [setpoint27, v_points27, arrow_points27, o_points27]

        setpoint28 = [(a, b)]
        v_points28 = [(a-2, b+2), (a+2, b-2)]
        arrow_points28 = [(a-3, b+3)]
        o_points28 = [(a-1, b+1), (a+1, b-1)]
        possible28 = [setpoint28, v_points28, arrow_points28, o_points28]

##########################################################
        setpoint29 = [(a, b)]
        v_points29 = [(a, b-2), (a, b+1), (a, b+3)]
        arrow_points29 = []
        o_points29 = [(a, b-1), (a, b+2)]
        possible29 = [setpoint29, v_points29, arrow_points29, o_points29]

        setpoint30 = [(a, b)]
        v_points30 = [(a+1, b+1), (a-2, b-2), (a+3, b+3)]
        arrow_points30 =[]
        o_points30 = [(a-1, b-1), (a+2, b+2)]
        possible30 = [setpoint30, v_points30, arrow_points30, o_points30]

        setpoint31 = [(a, b)]
        v_points31 = [(a-2, b), (a+1, b), (a+3, b)]
        arrow_points31 = []
        o_points31 = [(a-1, b), (a+2, b)]
        possible31 = [setpoint31, v_points31, arrow_points31, o_points31]

        setpoint32 = [(a, b)]
        v_points32 = [(a-2, b+2), (a+1, b-1), (a+3, b-3)]
        arrow_points32 = []
        o_points32 = [(a-1, b+1), (a+2, b-2)]
        possible32 = [setpoint32, v_points32, arrow_points32, o_points32]

        setpoint5_180 = [(a,b)]
        v_points5_180 = [(a, b-3), (a, b-1), (a, b+2)]
        arrow_points5_180 = []
        o_points5_180 = [(a, b+1), (a, b-2)]
        possible5_180 = [setpoint5_180, v_points5_180, arrow_points5_180, o_points5_180]

        setpoint33 = [(a, b)]
        v_points33 = [(a-1, b-1), (a-3, b-3), (a+2, b+2)]
        arrow_points33 = []
        o_points33 = [(a-2, b-2), (a+1, b+1)]
        possible33 = [setpoint33, v_points33, arrow_points33, o_points33]

        setpoint34 = [(a, b)]
        v_points34 = [(a-3, b), (a-1, b), (a+2, b)]
        arrow_points34 = []
        o_points34 = [(a-2, b), (a+1, b)]
        possible34 = [setpoint34, v_points34, arrow_points34, o_points34]

        setpoint35 = [(a, b)]
        v_points35 = [(a-3, b+3), (a-1, b+1), (a+2, b-2)]
        arrow_points35 = []
        o_points35 = [(a+1, b-1), (a-2, b+2)]
        possible35 = [setpoint35, v_points35, arrow_points35, o_points35]

###################################
        setpoint36 = [(a, b)]
        v_points36 = [(a,b-2), (a,b-1), (a,b+3)]
        arrow_points36 = []
        o_points36 = [(a, b+1), (a, b+2)]
        possible36 = [setpoint36, v_points36, arrow_points36, o_points36]

        setpoint37 = [(a, b)]
        v_points37 = [(a-1, b-1), (a-2, b-2), (a+3, b+3)]
        arrow_points37 = []
        o_points37 = [(a+1, b+1), (a+2, b+2)]
        possible37 = [setpoint37, v_points37, arrow_points37, o_points37]

        setpoint38 = [(a, b)]
        v_points38 = [(a-2, b), (a-1, b), (a+3, b)]
        arrow_points38 = []
        o_points38 = [(a+1, b), (a+2, b)]
        possible38 = [setpoint38, v_points38, arrow_points38, o_points38]

        setpoint39 = [(a, b)]
        v_points39 = [(a-1, b+1), (a-2, b+2), (a+3, b-3)]
        arrow_points39 = []
        o_points39 = [(a+1, b-1), (a+2, b-2)]
        possible39 = [setpoint39, v_points39, arrow_points39, o_points39]

        setpoint6_180 = [(a, b)]
        v_points6_180 = [(a, b - 3), (a, b + 1), (a, b + 2)]
        arrow_points6_180 = []
        o_points6_180 = [(a, b - 1), (a, b - 2)]
        possible6_180 = [setpoint6_180, v_points6_180, arrow_points6_180, o_points6_180]

        setpoint40 = [(a, b)]
        v_points40 = [(a+1, b+1), (a+2, b+2), (a-3, b-3)]
        arrow_points40 = []
        o_points40 = [(a-1, b-1), (a-2, b-2)]
        possible40 = [setpoint40, v_points40, arrow_points40, o_points40]

        setpoint41 = [(a, b)]
        v_points41 = [(a-3, b), (a+1, b), (a+2, b)]
        arrow_points41 = []
        o_points41 = [(a-1, b), (a-2, b)]
        possible41 = [setpoint41, v_points41, arrow_points41, o_points41]

        setpoint42 = [(a, b)]
        v_points42 = [(a+1, b-1), (a+2, b-2), (a-3, b+3)]
        arrow_points42 = []
        o_points42 = [(a-1, b+1), (a-2, b+2)]
        possible42 = [setpoint42, v_points42, arrow_points42, o_points42]



        possibles = [possible1, possible2, possible3, possible4, possible1_180, possible5,
                     possible6, possible7, possible8, possible9, possible10,
                     possible11, possible1_180,possible12, possible13, possible14, possible15,
                     possible16, possible17, possible18, possible3_180, possible19, possible20,
                     possible21, possible22, possible23, possible24, possible25, possible4_180,
                     possible26, possible27, possible28, possible29, possible30,
                     possible31, possible32, possible5_180, possible33, possible34, possible35,
                     possible36, possible37, possible38, possible39, possible6_180, possible40,
                     possible41, possible42]
        return possibles[number]


    def getpoints2(self, board, color):
        ans = []
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"
        possiblemoves35_white = self.findstates_helper(board, self.state_5_third_white, self.state_5_add_third, 5)
        possiblemoves45_white = self.findstates_helper(board, self.state_5_fourth_white, self.state_5_add_fourth, 5)
        possiblemoves4_white = possiblemoves35_white + possiblemoves45_white
        possiblemoves5_white = self.findstates_helper(board, self.state_4_fifth_white, self.state_4_add_fifth, 4)
        possiblemoves6_white = self.findstates_helper(board, self.state_4_sixth_white, self.state_4_add_sixth, 4)
        possiblemoves7_white = self.findstates_helper(board, self.state_5_sixth_white, self.state_5_add_sixth, 5)
        beforesorting_white =[possiblemoves4_white, possiblemoves5_white, possiblemoves7_white]
        combinepossiblemoves_white = []
        for i in range(len(beforesorting_white)):
            pickfirst = beforesorting_white[i]
            for j in range(len(pickfirst)):
                if self.nonOverlap(combinepossiblemoves_white, pickfirst[j]):
                    combinepossiblemoves_white.append(pickfirst[j])

        possiblemoves35_black = self.findstates_helper(board, self.state_5_third_black, self.state_5_add_third, 5)
        possiblemoves45_black = self.findstates_helper(board, self.state_5_fourth_black, self.state_5_add_fourth, 5)
        possiblemoves4_black = possiblemoves35_black + possiblemoves45_black
        possiblemoves5_black = self.findstates_helper(board, self.state_4_fifth_black, self.state_4_add_fifth, 4)
        possiblemoves6_black = self.findstates_helper(board, self.state_4_sixth_black, self.state_4_add_sixth, 4)
        possiblemoves7_black = self.findstates_helper(board, self.state_5_sixth_black, self.state_5_add_sixth, 5)
        # print possiblemoves4_white
        # print possiblemoves5_white
        beforesorting_black = [possiblemoves4_black, possiblemoves5_black, possiblemoves7_black]
        combinepossiblemoves_black = []
        for i in range(len(beforesorting_black)):
            pickfirst = beforesorting_black[i]
            for j in range(len(pickfirst)):
                if self.nonOverlap(combinepossiblemoves_black, pickfirst[j]):
                    combinepossiblemoves_black.append(pickfirst[j])
        if color == "W":
            for i in range(len(combinepossiblemoves_white)):
                point = combinepossiblemoves_white[i]
                row = point[0]
                col = point[1]
                for k in range(48):
                    for l in range(48):
                        if l%8 != k%8:
                            possibleFirst = self.getpossible(k, row, col)
                            possibleSecond = self.getpossible(l, row, col)
                            first_bool = self.templatefinal(board, color, possibleFirst)
                            second_bool = self.templatefinal(board, color, possibleSecond)
                            if first_bool and second_bool:
                                if self.nonOverlap(ans, (row, col)):
                                    ans.append((row, col))
                            first_bool = False
                            second_bool = False
        if color == "B":
            for i in range(len(combinepossiblemoves_black)):
                point = combinepossiblemoves_black[i]
                row = point[0]
                col = point[1]
                for k in range(48):
                    for l in range(48):
                        if l%8 != k%8:
                            possibleFirst = self.getpossible(k, row, col)
                            possibleSecond = self.getpossible(l, row, col)
                            first_bool = self.templatefinal(board, color, possibleFirst)
                            second_bool = self.templatefinal(board, color, possibleSecond)
                            if first_bool and second_bool:
                                if self.nonOverlap(ans, (row, col)):
                                    ans.append((row, col))
                            first_bool = False
                            second_bool = False
        return ans

    def testpoint(self, board, color, (a,b)):
        board = self.board
        row = a
        col = b
        for k in range(48):
            for l in range(48):
                if l%8 != k%8:
                    possibleFirst = self.getpossible(k, row, col)
                    possibleSecond = self.getpossible(l, row, col)
                    first_bool = self.templatefinal(board, color, possibleFirst)
                    second_bool = self.templatefinal(board, color, possibleSecond)
                    if first_bool or second_bool:
                        print possibleFirst, k
                        print possibleSecond, l
                        print first_bool, second_bool
                    if first_bool and second_bool:
                        return True
                                # else:
                                #     continue
        return False

    def templatefinal(self, board, color, possible):
        if color == "W":
            color_opp = "B"
        else:
            color_opp = "W"
        setpoint = possible[0]
        v_points = possible[1]
        arrow_points = possible[2]
        o_points = possible[3]

        for i in range(len(v_points)):
            if not (0 <= v_points[i][0] < 15 and 0 <= v_points[i][1] < 15):
                return False
        if len(arrow_points) != 0:
            if not (0 <= arrow_points[0][0] < 15 and 0 <= arrow_points[0][1]< 15):
                return False
        for i in range(len(o_points)):
            if not (0 <= o_points[i][0] < 15 and 0 <= o_points[i][1] < 15):
                return False


        if board[setpoint[0][0]][setpoint[0][1]] == ",":
            first_bool = True
        else:
            first_bool = False
        # first_bool = (board[setpoint[0][0]][setpoint[0][1]] == ",")

        second_bool = False
        for i in range(len(v_points)):
            if not (board[v_points[i][0]][v_points[i][1]] == color or board[v_points[i][0]][v_points[i][1]] == ","):
                break
            if i == len(v_points)-1:
                second_bool = True


        third_bool = True
        if len(arrow_points) != 0:
            if (board[arrow_points[0][0]][arrow_points[0][1]] == "," or
                          board[arrow_points[0][0]][arrow_points[0][1]] == "B" or
                          board[arrow_points[0][0]][arrow_points[0][1]] == "W"):
                third_bool = True
            else:
                third_bool = False
            # third_bool = (board[arrow_points[0][0]][arrow_points[0][1]] == "," or
            #               board[arrow_points[0][0]][arrow_points[0][1]] == "B" or
            #               board[arrow_points[0][0]][arrow_points[0][1]] == "W")

        if (board[o_points[0][0]][o_points[0][1]] == color and board[o_points[1][0]][o_points[1][1]] == color):
            fourth_bool = True
        else:
            fourth_bool = False

        combine_boolean = (first_bool and second_bool and third_bool and fourth_bool)

        if combine_boolean:
            return combine_boolean
        else:
            return False

    # def seeAhead(self, board):
    #     board2 = deepcopy(self.board)
    #     possiblemoves1_white = self.findstates_helper(board, self.state_5_first_white, self.state_5_add_first, 5)
    #     possiblemoves2_white = self.findstates_helper(board, self.state_6_second_white, self.state_6_add_second, 6)
    #     possiblemoves3_white = self.getpoints2(board, "W")
    #     # combine fourth  priority
    #     possiblemoves35_white = self.findstates_helper(board, self.state_5_third_white, self.state_5_add_third, 5)
    #     possiblemoves45_white = self.findstates_helper(board, self.state_5_fourth_white, self.state_5_add_fourth, 5)
    #     possiblemoves4_white = possiblemoves35_white + possiblemoves45_white
    #     possiblemoves5_white = self.findstates_helper(board, self.state_4_fifth_white, self.state_4_add_fifth, 4)
    #     possiblemoves6_white = self.findstates_helper(board, self.state_4_sixth_white, self.state_4_add_sixth, 4)
    #     # possiblemoves7_white = self.findstates_helper(board, self.state_5_sixth_white, self.state_5_add_sixth, 5)
    #
    #     possiblemoves1_black = self.findstates_helper(board, self.state_5_first_black, self.state_5_add_first, 5)
    #     possiblemoves2_black = self.findstates_helper(board, self.state_6_second_black, self.state_6_add_second, 6)
    #     possiblemoves3_black = self.getpoints2(board, "B")
    #     possiblemoves35_black = self.findstates_helper(board, self.state_5_third_black, self.state_5_add_third, 5)
    #     possiblemoves45_black = self.findstates_helper(board, self.state_5_fourth_black, self.state_5_add_fourth, 5)
    #     possiblemoves4_black = possiblemoves35_black + possiblemoves45_black
    #     possiblemoves5_black = self.findstates_helper(board, self.state_4_fifth_black, self.state_4_add_fifth, 4)
    #     possiblemoves6_black = self.findstates_helper(board, self.state_4_sixth_black, self.state_4_add_sixth, 4)
    #
    #     seeAhead = []
    #     before_sorting = [possiblemoves4_white, possiblemoves4_black, possiblemoves5_white, possiblemoves5_black]
    #     for i in range(len(before_sorting)):
    #         pickfirst = before_sorting[i]
    #         for j in range(len(pickfirst)):
    #             if self.nonOverlap(seeAhead, pickfirst[j]):
    #                 seeAhead.append(pickfirst[j])
    #
    #     if len(seeAhead) == 0:
    #         return self.simplePlay(board)
    #     print seeAhead
    #     valuelist = []
    #     for i in range(len(seeAhead)):
    #         valuelist.append(self.counteachPrioirty(self.makeMove2(board2, "W", (seeAhead[i])), "W"))
    #         board2 = deepcopy(self.board)
    #     highest = 0
    #     print valuelist
    #     for i in range(len(valuelist)):
    #         if valuelist[i] >= highest:
    #             highest = i
    #     return seeAhead[highest]

test = gomoku()
#
test.playingGame()
# test.seeAhead(test.board)
# def printboard3(board):
#     context = ""
#     for i in range(15):
#         for j in range(15):
#             context = context + " " + str(board[i][j])
#         print context
#         context = ""
#     print "   "


# test.getpossible(1, 5, 5)

# print test.templatefinal(test.board, (4,5), "W", test.getpossible(1, 5, 5))

# print test.templatefinal(test.board, "W", test.getpossible(0, 10, 10))

# print test.getpoints(test.board, "W")

# print test.getpoints2(test.board, "W")

# print test.testpoint(test.board, "W", (4,7))

# print -220120 > -204556