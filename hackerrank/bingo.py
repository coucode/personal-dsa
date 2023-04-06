def getBingoNumber(mat, arr):
    rows = len(mat)
    cols = len(mat[0])
    diagonals = rows == cols
    
    mat_table = {}
    for i in range(len(mat)):
        this_row = mat[i]
        for j in range(len(this_row)):
            value = this_row[j]
            mat_table[value] = [i, j]
    
    for num in arr:
        current_row = mat_table[num][0]
        current_col = mat_table[num][1]
        mat_table[num] = 0
        
        bingo = True
        for x in range(len(mat[current_row])):
            row_val = mat[current_row][x]
            if mat_table[row_val] != 0:
                bingo = False
        if bingo == True:
            return num
        
        for y in range(rows):
            col_val = mat[y][current_col]
            if mat_table[col_val] != 0:
                bingo = False
        if bingo == True:
            return num
        
        d_bingo = True
        if (diagonals == True):
            w = 0
            while w < rows:
                d_val = mat[w][w]
                if mat_table[d_val] != 0:
                    d_bingo = False
                w += 1
            if d_bingo == True:
                return num