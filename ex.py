# 1

def SumMultiples(n) :
    a = int(n / 3)
    #print (a)
    sum = 0
    
    #sum of all multiples of 3
    for num in range(1, a+1):
        sum = sum + 3 * num

    #sum of all multiples of 5
    b = int(n/5)
    for num in range(1, b+1):
        sum = sum + 5 * num

    #subtract of all multiples of 15
    c = int(n/15)
    for num in range(1, c+1):
        sum = sum - 15 * num

    print (sum)

SumMultiples(1000)


# 2 find fibonacci
def F(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return F(n-1) + F(n-2)

F(3)
print ("8th Fibonacci is " + str(F(8)))
#print (F(8))
#print (F(50))

# 3 find deriv

def f(x) :
    return 2 * (x**3)

def deriv(f, x) :
    deltaX = 0.000001
    return (f(x + deltaX) - f(x))/deltaX

print (deriv(f,5))

# 4 multiply matrix

#find length of matrix

matrix = [[1,2,3], [4,5,6],[7,8,9], [10,11,12]]

print (len(matrix))
print (len(matrix[0]))
# column number is len(matrix)
# row number is len(matrix[0])
print(matrix)

def matrixMult(a, b):
    row_1 = len(a)
    col_1 = len(a[0])

    row_2 = len(b)
    col_2 = len(b[0])
    if col_1 != row_2:
        return print("not valid matrices")

    for number in range(0,
    return ans
matrixMult([[1,2,3],[1,2,3]], [[1],[2],[3],[4]])

# 5 levenshtein distance
