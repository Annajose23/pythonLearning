def mine_sweeper(bombs, num_rows, num_cols):
    Matrix = [[0 for x in range(num_cols)] for y in range(num_rows)] 
    for bomb in bombs:
        row_i = bomb[0]
        col_i = bomb[1]
        Matrix[row_i][col_i] = -1
        for i in range(row_i-1,row_i+2):
            for j in range(col_i-1, col_i+2):
                if Matrix[i][j] != -1 and 0 <= i < num_rows and 0 <= j < num_cols:
                    Matrix[i][j] += 1
    print(Matrix)


mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)