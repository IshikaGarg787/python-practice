# Define matrices A (2x3) and B (3x2)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
r1=len(A)
c1=len(A[0])
r2=len(B)
c2=len(B[0])
# Result matrix C will be of size 2x2 (since A is 2x3 and B is 3x2)
C = [[0, 0], [0, 0]]

# Multiply matrices A and B
for i in range(r1):  # 2 rows in A
    for j in range(c2):  # 2 columns in B
        C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + A[i][2] * B[2][j]

# Print the result
for row in C:
    print(*row,sep='\t')