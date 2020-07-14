# write an algorithm such that if an element in an Mxn matrix is 0, its entire row and
# column are set to 0



# match
# go through it

# plan
# iterate through the matrix once
# find all the zeroes
# for each zero, mark its first element row and column to zero

# after marking the zeroes, go through the rows and columns
# for each row and column in first row and column
    # set all subsequeent to zero
# if the first element in the matrix is 0, then set entire row



def zero_matrix(matrix):
        row_zero = False
        col_zero = False
        for i in range(0,len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True
                
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_zero = True
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
                    
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
                    
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
                
        return matrix

# runs at O(N + M) time
