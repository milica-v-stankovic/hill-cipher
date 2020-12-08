import numpy as np

class Matrix(object):

    def __init__(self, matrix, n, m):
        self.matrix = matrix
        self.n = n
        self.m = m

    def getDeterminant(self):

        determinant = 0
        
        x = self.matrix[0][0] * ((self.matrix[1][1] * self.matrix[2][2]) - (self.matrix[1][2] * self.matrix[2][1]))
        y = self.matrix[0][1] * ((self.matrix[1][0] * self.matrix[2][2]) - (self.matrix[1][2] * self.matrix[2][0]))
        z = self.matrix[0][2] * ((self.matrix[1][0] * self.matrix[2][1]) - (self.matrix[1][1] * self.matrix[2][0]))

        determinant = x - y + z

        return determinant

    def getTransposeMatrix(self):

        transposeMatrix = np.zeros((self.n, self.m))

        for i in range(self.n):
            for j in range(self.m):
                transposeMatrix[i][j] = self.matrix[j][i]
        
        return transposeMatrix

    def getAdjacencyMatrix(self):

        adjacencyMatrix = np.zeros((3, 3))
        sign = 1
        for i in range(3):
            for j in range(3):
                indexi = 0
                adji = np.zeros((2, 2))
                for k in range(3):
                    if k == i:
                        continue
                    indexj = 0
                    for h in range(3):
                        if h == j:
                            continue
                        adji[indexi][indexj] = self.matrix[k][h]
                        indexj += 1
                    indexi += 1
                adjacencyMatrix[i][j] = ((adji[0][0] * adji[1][1]) - (adji[0][1] * adji[1][0])) * sign
                sign *= -1

        print(adjacencyMatrix)
        return adjacencyMatrix