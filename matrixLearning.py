def rotate(arr, r):
    return arr[r % len(arr):] + arr[:r % len(arr)]


def matrixRotation(matrix, r):
    M, m, n = list(matrix), len(matrix), len(matrix[0])
    for i in range(min(m, n)//2):
        R = rotate(matrix[i][i:n-1-i] + [matrix[j][n-1-i] for j in range(i, m-1-i)] +
                   matrix[m-1-i][n-1-i:i:-1] + [matrix[j][i] for j in range(m-1-i, i, -1)], r)
        M[i][i:n-1-i], M[m-1-i][n-1-i:i:-1] = R[:n-1-2*i], R[m+n-2-4*i:m+2*n-3-6*i]
        for j in range(m-1-2*i):
            M[i+j][n-1-i] = R[n-1-2*i+j]
            M[m-1-i-j][i] = R[m+2*n-3-6*i+j]
    [print(*r) for r in M]


matrix = [
    [1, 2, 3, 4],
 	[5, 6, 7, 8],
 	[9, 10, 11, 12],
 	[13, 14, 15, 16]
]
matrixRotation(matrix,1)
