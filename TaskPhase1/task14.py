#Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range (i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
n = int(input("Enter the size of the matrix (n x n): "))
matrix = []
print("Enter the elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
rotated_matrix = rotate(matrix)
print("Rotated Matrix by 90° clockwise:")
for row in rotated_matrix:
    print(row)