#Python code to perform elimination on a matrix
#Sample Matrix
A = [[0.0,2.0,3.0],
     [4.0,5.0,6.0],
     [7.0,8.0,9.0]]
#Sample b
b = [5,11,17]

solutionVector = [0,0,0]

# Convert matrix A into Upper Triangular shape(zeroes below main diagonal)
# If matrix A is m x n where m != n , then U is Echelon form
def AtoU(A,displayProcess):
    for p in range(2):
        i = 1
        if A[p][p] == 0: # Zero Pivot
            row = p
            while(A[row][p] == 0): # Check next available row with a non zero pivot
                if row == len(A)-1:
                    continue
                else:
                    row+=1
            if(displayProcess):
                print("Pivot = 0, Row exchange", p ," and ",row)
            rowExchange(p,row,A)

        for e in range(p+1,len(A)):
            factor = A[e][p]/A[p][p]
            elimination(A,e,p,factor,displayProcess) # Perfom elimination
            change(A,e,p,factor,i,displayProcess)    # Modify elements on the rest of the row
            i+=1
    if(displayProcess):
        printA(A)
    return A

def elimination(A,row,col,factor, displayProcess):
    A[row][col] = A[row][col] - (factor*A[col][col])
    if(displayProcess):
        print("Eliminated A",row,col)

def change(A,row,col,factor,i,displayProcess):
    while(col!=len(A[row])-1):
        A[row][col+1] = A[row][col+1] - (factor*A[row-i][col+1])
        col += 1
        if (displayProcess):
            print("Changed A",row,col)

def printA(A):
    print("A-->U")
    print("-----------------------------")
    for r in range(len(A)):
        for c in range(len(A[r])):
            print(str(A[r][c]), end= " ")
        print()
    print("-----------------------------")

def rowExchange(p, row, A):

    for i in range(len(A[p])):
        exch = A[p][i]
        A[p][i] = A[row][i]
        A[row][i] = exch



# Creates an Augmented matrix A|b
def AugmnentedA(A,b):
    Ab = A
    for row in range(len(A)):
        Ab[row].append(b[row])
    return Ab

# Starts the recursive call to apply back substitution
def backSubs(A):
    RecursiveSub(A,len(A)-1,len(A[0])-2)

def RecursiveSub(A,r,c):
    if r<0:
        return
    dividend = A[r][len(A[r])-1]
    col = len(A[r])-2
    while(col != c):
        dividend-=A[r][col]
        col-=1
    solutionVector[r] = dividend/A[r][c]
    row = r
    while(row>=0):
        row-=1
        A[row][c] = A[row][c] * solutionVector[r]
    r-=1
    c-=1
    RecursiveSub(A,r,c)


backSubs(AtoU(AugmnentedA(A,b),True)) # True to display the process to solve system of linear equations
print("SOLUTION : ", solutionVector)
