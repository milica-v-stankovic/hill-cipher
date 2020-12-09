from HillCipher.matrix import Matrix
from HillCipher.MathOperations import computeGDC, getMultiplicativeInverse

class Key(object):

    def __init__(self, value, modulo, blockSize):
        self.matrix = Matrix(value, blockSize, blockSize)
        self.modulo = modulo
        self.blockSize = blockSize

    def returnKeyValue(self):
        return self.matrix.matrix

    def checkKeyValidity(self):
        
        determinant = self.matrix.getDeterminant()
        if (determinant == 0):
            return False
        
        if (computeGDC(determinant, self.modulo) != 1):
            return False

        self.determinant = determinant

        return True

    def getInverseKey(self):

        keyDeterminant = self.matrix.getDeterminant() % self.modulo
        transposeKey = self.matrix.getTransposeMatrix()
        adjacencyKey = self.matrix.getAdjacencyMatrix()
        multiplicativeInverse = getMultiplicativeInverse(keyDeterminant, self.modulo)

        modularInverseKey = []

        for i in range(self.blockSize):
            newRow = []
            for j in range(self.blockSize):
                newElement = (adjacencyKey[i][j] % self.modulo)
                newRow.append(newElement)
            modularInverseKey.append(newRow)

        inverseKey = []
        for j in range(self.blockSize):
            newColumn = []
            for i in range(self.blockSize):
                newElement = int((modularInverseKey[i][j] * multiplicativeInverse) % self.modulo)
                newColumn.append(newElement)
            inverseKey.append(newColumn)

        return inverseKey