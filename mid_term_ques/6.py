class MatrixDimensionError(Exception):
    pass

class Matrix:
    def __init__(self, data):
        self.data = data  # 2D list
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError("Matrices must have the same dimensions for addition")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise MatrixDimensionError("Invalid dimensions for matrix multiplication")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_value = 0
                for k in range(self.cols):
                    sum_value += self.data[i][k] * other.data[k][j]
                row.append(sum_value)
            result.append(row)
        return Matrix(result)
    
    def __eq__(self, other):
        return self.data == other.data

    @property
    def transpose(self):
        result = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.data[j][i])
            result.append(row)
        return Matrix(result)

# Test Input
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print((m1 + m2).data)  # [[6, 8], [10, 12]]
print((m1 * m2).data)  # [[19, 22], [43, 50]]
print(m1.transpose.data)  # [[1, 3], [2, 4]]
