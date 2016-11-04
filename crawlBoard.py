## Crawling down the board by moving left, right and diagonally . Optimized solution to get rid of memory issues when given large number inputs
def  krakenCount(m, n):
    if(m <= 0 or n <= 0):
        return 0
    elif(m==1 and n==1):
        return 1
    temp = [[0]*n for _ in range(m)]
    for i in range(len(temp)):
        temp[i][0] = 1
    for j in range(n):
        temp[0][j] =1
    i = 1
    while(i < m):
        if(i %30 == 0):
            del temp[0:i-1] ## deleting the earlier parts of the array that are not needed for memory optimization for every 30 iterations
            m = m-i+1
            i = 1
        for y in range(1,n):
            temp[i][y] = temp[i-1][y] + temp[i][y-1]+temp[i-1][y-1]
        i += 1
    return temp[len(temp)][n-1]
