##General Search Procedure

# def makeNode(state, parent, depth, pathCost):
#     return [state, parent, depth, pathCost]
#
# def generalSearch(queue, limit, numRuns):
#     if queue == []:
#         return False
#     elif testProcedure(queue[0])
#         :outputProcedure(numRuns,  queue[0])
#     elif limit == 0:
#         print "Limit reached"
#     else:
#         limit -= 1
#         numRuns += 1
#         generalSearch(expandProcedure(queue[0], queue[1:len(queue)]), limit, numRuns)

##Jaemin Jung, hw2, colaboratied with Sunghyun Lee, Soon Kwon, Min Park, Bumlak Kim
#Part I

import copy

class puzzle:
    def __init__(self):
        self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
        self.visited = []
        self.swapindex = []
        self.frontier = []

    def is_this_goal(self, a, goal):
        if len(a) == 2:
            if a[0] == goal:
                return True
            else:
                return False
        else:
            if a == goal:
                return True
            else:
                return False
        # count = 1
        # is_goal = True
        # col = len(a[0])
        # row = len(a)
        # for i in range(0, row):
        #     for j in range(0, col):
        #         if (i == row - 1) and (j == col - 1):
        #             is_goal= True
        #         elif a[i][j] != count:
        #             is_goal = False
        #             break
        #         count = count + 1
        #     else:
        #         continue
        #     break
        # return is_goal

    def printing(self, a):
        string = " "
        if len(a) == 2:
            col1 = len(a[0][0])
            row1 = len(a[0])
            for i in range(0, col1):
                for j in range(0, row1):
                    string = string + " " + str(a[0][i][j])
                print string
                string = " "
        else:
            col = len(a[0])
            row = len(a)
            for i in range(0, col):
                for j in range(0, row):
                    string = string + " " + str(a[i][j])
                print string
                string = " "

    def is_visited(self, matrix):
        for i in range(0, len(self.visited)):
            if len(matrix) == 2:
                if len(self.visited[i]) == 2:
                    if matrix[0] == self.visited[i][0]:
                        return True
                elif len(self.visited[i]) == 1:
                    if matrix[0] == self.visited[i]:
                        return True
            elif len(matrix) == 1:
                if len(self.visited[i]) == 2:
                    if matrix == self.visited[i][0]:
                        return True
                elif len(self.visited[i]) == 1:
                    if matrix == self.visited[i]:
                        return True
        return False
        # for i in range(0, len(self.visited)):
        #     if a == self.visited[i]:
        #         return True
        # return False

    def is_frontier(self, a):
        for i in range(0, len(self.frontier)):
            if a == self.frontier[i]:
                return True
        return False

    def find_empty(self, a):
        if len(a) == 2:
            for i in range(0, len(a[0])):
                for j in range(0, len(a[0][0])):
                    if a[0][i][j] == " ":
                        return i, j
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                if a[i][j] == " ":
                    return i, j

    def swap_possible(self, a):
        if len(a) == 2:
            e = self.find_empty(a)
            for i in range(0, len(a[0])):
                for j in range(0, len(a[0][0])):
                    if abs(i - e[0]) + abs(j - e[1]) == 1:
                        self.swapindex.append([i, j])
        else:
            e = self.find_empty(a)
            for i in range(0, len(a)):
                for j in range(0, len(a[0])):
                    if abs(i - e[0]) + abs(j - e[1]) == 1:
                        self.swapindex.append([i, j])

    def swap(self, a, rownum1, colnum1, rownum2, colnum2):
        if len(a) != 2:
            temp = a[rownum1][colnum1]
            a[rownum1][colnum1] = a[rownum2][colnum2]
            a[rownum2][colnum2] = temp
            return a
        else:
            temp = a[0][rownum1][colnum1]
            a[0][rownum1][colnum1] = a[0][rownum2][colnum2]
            a[0][rownum2][colnum2] = temp
            return a


    def push_to_f(self, a):
        self.swap_possible(a)
        temp = copy.deepcopy(a)
        row2 = self.find_empty(a)[0]
        col2 = self.find_empty(a)[1]
        for i in range(0, len(self.swapindex)):
            val_to_swap = self.swap(temp, self.swapindex[i][0], self.swapindex[i][1], row2, col2)
            if self.is_visited(val_to_swap) == False:
                self.frontier.append(val_to_swap)
            temp = copy.deepcopy(a)

    # def solution(self, a):
    #     self.printing(a)
    #     print " "
    #     if self.is_this_goal(a) == True:
    #         self.printing(a)
    #         return True
    #     else:
    #         self.visited.append(a)
    #     self.push_to_f(a) #size of 2, 3, 4
    #     print "swapIndex", self.swapindex
    #     self.swapindex = []
    #     print "swapIndex", self.swapindex
    #     print len(self.frontier), "frontier", self.frontier
    #     print len(self.visited), "visited", self.visited
    #     b = self.frontier.pop(0)
    #     self.solution(b)
    # using recursion, the algorithm makes too deep recursion, it automatically stop algorithm.
    def testUninformedSearch(self, a, goal, limit):
        self.printing(a)
        print " "
        numofvisit = len(self.visited)
        count = 1
        if self.is_this_goal(a, goal) == True:
            print "find goalState"
            self.printing(a)
            return True
        else:
            self.visited.append(a)
        self.push_to_f(a)
        self.swapindex = []
        while (len(self.frontier) != 0):
            b = self.frontier.pop(0) #if pop(0) - BFS, if pop() - DFS
            self.printing(b)
            self.visited.append(b)
            if self.is_this_goal(b, goal) == True:
                print " find the goal state!"
                self.printing(b)
                return True
                break
            else:
                self.swapindex = []
                print " number of tried :", count
                print " "
                # print len(self.frontier), "frontier", self.frontier
                # print len(self.visited), "visited", self.visited
                # print len(self.visited)
                self.push_to_f(b)
                count = count + 1
            if count > limit:
                print "exceed limit"
                return None
                break

    #Part II - a* search
    def heuristic(self, matrix, goal):
        # Calculates how far each tile is from its goal state, and sums those distances
        if len(matrix) != 2:
            sum = 0
            for i in range(0, len(goal)):
                for j in range(0, len(goal)):
                    tile = goal[i][j]
                    for k in range(0, len(matrix)):
                        for l in range(0, len(matrix)):
                            if matrix[k][l] == tile:
                                sum += (k - i) * (k - i) + (j - l) * (j - l)
            return sum
        else:
            sum = 0
            for i in range(0, len(goal)):
                for j in range(0, len(goal)):
                    tile = goal[i][j]
                    for k in range(0, len(matrix[0])):
                        for l in range(0, len(matrix[0])):
                            if matrix[0][k][l] == tile:
                                sum += (k - i) * (k - i) + (j - l) * (j - l)
            return sum

    #count the number of tile that does not match with goalState
    def heuristic1(self, matrix, goal):
        count = 0
        num = 1 #first low match -> -5
        if len(matrix) != 2:
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix)):
                    if matrix[i][j] != goal[i][j]:
                        count = count + 2
        else:
            for i in range(0, len(matrix[0])):
                for j in range(0, len(matrix[0])):
                    if matrix[0][i][j] != goal[i][j]:
                        count = count + 2
        # if  one of 1, 2, 3 tile is right, it gives - 5 points
        if len(matrix) != 2:
            for i in range(0, len(matrix)):
                if matrix[0][i] == num:
                    count = count - 5
        else:
            for i in range(0, len(matrix[0])):
                if matrix[0][0][i] == num:
                    count = count - 5
        #if all of first row of tiles are correct, it give -10 points
        if len(matrix) != 2:
            if matrix[0][0] == 1 and matrix[0][1] == 2 and matrix[0][2] == 3:
                count = count - 10
        else:
            if matrix[0][0][0] == 1 and matrix[0][0][1] == 2 and matrix[0][0][2] == 3:
                count = count - 10
        return count

    def combine_heuristic(self, matrix, goal):
        return self.heuristic(matrix, goal) + self.heuristic1(matrix, goal)

    def has_hamming_d(self, matrix):
        if len(matrix) != 2:
            matrix = (matrix, self.heuristic(matrix, self.goalState))
            return matrix
        else:
            return matrix

    def push_to_f_star(self, a):
        if len(a) != 2:
            self.swap_possible(a)
            temp = copy.deepcopy(a)
            row2 = self.find_empty(a)[0]
            col2 = self.find_empty(a)[1]
            for i in range(0, len(self.swapindex)):
                val_to_swap = self.swap(temp, self.swapindex[i][0], self.swapindex[i][1], row2, col2)
                if self.is_visited(val_to_swap) == False:
                    self.frontier.append((val_to_swap, self.combine_heuristic(a, self.goalState)))
                temp = copy.deepcopy(a)
        else:
            self.swap_possible(a)
            temp = copy.deepcopy(a)
            row2 = self.find_empty(a)[0]
            col2 = self.find_empty(a)[1]
            # print temp, " is temp"
            # print self.swapindex, "is swapindex"
            # print len(self.swapindex), "length of swapindex"
            for i in range(0, len(self.swapindex)):
                val_to_swap = self.swap(temp, self.swapindex[i][0], self.swapindex[i][1], row2, col2)
                # print val_to_swap, "is val_to_swap"
                if self.is_visited(val_to_swap) == False:
                    if len(self.frontier) == 0:
                        self.frontier.append((val_to_swap[0], self.combine_heuristic(val_to_swap[0], self.goalState)))
                    else:
                        for j in range(0, len(self.frontier)):
                            if self.frontier[j][1] > self.combine_heuristic(val_to_swap, self.goalState):
                                self.frontier.insert(j, (val_to_swap[0], self.combine_heuristic(val_to_swap[0], self.goalState)))
                                break
                            elif j == len(self.frontier)-1:
                                self.frontier.append((val_to_swap[0], self.combine_heuristic(val_to_swap[0], self.goalState)))
                temp = copy.deepcopy(a)

    def testInformedSearch(self, matrix, goal, limit):
        matrix = self.has_hamming_d(matrix)
        self.printing(matrix)
        numofvisit = len(self.visited)
        count = 1
        if numofvisit > limit:
            print "exceed limit"
            return None
        if self.is_this_goal(matrix, goal) == True:
            print " find goalState!"
            self.printing(matrix)
            return True
        else:
            self.visited.append(matrix)
        self.push_to_f_star(matrix)
        self.swapindex = []
        # print matrix
        # print len(self.frontier), "frontier", self.frontier
        # print len(self.visited), "visited", self.visited
        while (len(self.frontier) != 0):
            b = self.frontier.pop(0) # pop the element that has lowest hammington Distance
            self.visited.append(b)
            if self.is_this_goal(b, goal) == True:
                print " find goalState"
                self.printing(b)
                return True
                break
            else:
                self.swapindex = []
                print " number of tried : ", count
                self.printing(b)
                # print len(self.frontier), "frontier"#, self.frontier
                # print len(self.visited),  " , ", b[1]# "visited", self.visited
                self.push_to_f_star(b)
                count = count + 1
            if count > limit:
                print "exceed limit"
                return None
                break

    def makeState(self, nw, n, ne, w, c, e, sw, s, se):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        matrix[0][0] = nw
        matrix[0][1] = n
        matrix[0][2] = ne
        matrix[1][0] = w
        matrix[1][1] = c
        matrix[1][2] = e
        matrix[2][0] = sw
        matrix[2][1] = s
        matrix[2][2] = se
        return matrix

goalState = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
# state1 = [[1, 2, " "], [3, 4, 5], [7, 8, 6]]
state1 = [[" ", 8, 7], [6, 5, 4], [3, 2, 1]]
state2 = [[1, 2, 3], [" ", 5, 4], [7, 8, 6]]
state3 = [[1, 2, 3], [4, 8, " "], [7, 5, 6]]
state4 = [[5, 2, 7], [6, 4, 3], [1, " ", 8]]
test = puzzle()
initialState = test.makeState(8, 7, 6, 5, 4, 3, 2, 1, " ")
goalState = test.makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
test.testUninformedSearch(initialState, goalState, 5000)
# test.testInformedSearch(initialState, goalState, 5000)