#FOR LONGEST COMMON SUBSEQUENCE

def LCSubb(X, Y, m, n):
    #to declare matrix of 0 entries
    LCSub = [[0 for k in range(m+1) for j in range(n+1)]]

    for i in range(m+1):
        for j in range(n+1):
            if ( i==0j or j==0 ):
                LCSub[i][j] = 0
            elif ( X[i-1] == Y[j-1]):
                LCSub[i][j] = LCSub[i-1][j-1] + 1
            else :
                LCSub

