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
        print(keyDeterminant)
        transposeKey = self.matrix.getTransposeMatrix()
        print(transposeKey)
        adjacencyKey = self.matrix.getAdjacencyMatrix()
        print(adjacencyKey)
        multiplicativeInverse = getMultiplicativeInverse(keyDeterminant, self.modulo)
        print(multiplicativeInverse)

        modularInverseKey = []

        for i in range(self.blockSize):
            newRow = []
            for j in range(self.blockSize):
                newElement = (adjacencyKey[i][j] % self.modulo)
                newRow.append(newElement)
            modularInverseKey.append(newRow)

        inverseKey = []
        print(modularInverseKey)
        for i in range(self.blockSize):
            newRow = []
            for j in range(self.blockSize):
                newElement = int((modularInverseKey[i][j] * multiplicativeInverse) % self.modulo)
                newRow.append(newElement)
            inverseKey.append(newRow)

        print(inverseKey)
        return inverseKey